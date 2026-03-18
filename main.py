import os
import markdown
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from scraper import get_market_data
from analyzer import analyze_market_data

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/analyze/{sector}/", response_class=HTMLResponse)
@app.get("/analyze/{sector}", response_class=HTMLResponse)
async def analyze(request: Request, sector: str, download: bool = False):
    data = get_market_data(sector)
    report_md = analyze_market_data(sector, data)

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