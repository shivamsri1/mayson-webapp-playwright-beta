import os
from playwright.sync_api import sync_playwright

def convert_html_to_pdf(html_path, pdf_path):
    print(f"Converting {html_path} to {pdf_path}...")
    
    # Ensure absolute path with file:// schema
    abs_html_path = f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Go to the HTML report
        page.goto(abs_html_path, wait_until="networkidle")
        
        # Inject CSS to make the pytest-html report print better
        page.add_style_tag(content="""
            @media print {
                body { background: white !important; font-size: 12px; }
                .summary { page-break-inside: avoid; }
                .results-table { width: 100%; border-collapse: collapse; }
                .results-table th, .results-table td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                /* Hide things we don't need in PDF */
                input[type=checkbox], label { display: none !important; }
                .log { display: block !important; }
            }
        """)
        
        # Wait a second for styles/JS to settle
        page.wait_for_timeout(1000)
        
        # Generate the PDF
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "20px", "right": "20px", "bottom": "20px", "left": "20px"}
        )
        
        browser.close()
        print(f"✅ Successfully generated PDF: {pdf_path}")

if __name__ == "__main__":
    html_file = "reports/report.html"
    pdf_file = "reports/test_report.pdf"
    
    if not os.path.exists("reports"):
        print("Reports directory not found. Please run pytest first.")
    elif not os.path.exists(html_file):
        print(f"HTML report not found at {html_file}. Run pytest --html={html_file} --self-contained-html first.")
    else:
        convert_html_to_pdf(html_file, pdf_file)
