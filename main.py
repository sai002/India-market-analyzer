import os
import markdown
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from dotenv import load_dotenv

from scraper import get_market_data
from analyzer import analyze_market_data


current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, '.env'))
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))


app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/analyze/{sector}/", response_class=HTMLResponse)
@app.get("/analyze/{sector}", response_class=HTMLResponse)
@limiter.limit("5/minute")
async def analyze(request: Request, sector: str, download: bool = False):
    # Fetch and Analyze data
    data = get_market_data(sector)
    report_md = analyze_market_data(sector, data)

    if "Error" in report_md and not data:
        raise HTTPException(status_code=500, detail="AI Analysis Failed or No Data Found")

    
    if download:
        return Response(
            content=report_md,
            media_type="text/markdown",
            headers={"Content-Disposition": f"attachment; filename={sector}_report.md"}
        )


    html_report = markdown.markdown(report_md)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "sector": sector.capitalize(),
        "report_html": html_report
    })