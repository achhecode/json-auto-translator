def save_source(driver, filename=None, include_metadata=True):
    """
    Enhanced page source saver
    
    Args:
        driver: WebDriver instance
        filename: Custom filename (auto-generates if None)
        include_metadata: Add metadata comments at top
    """
    if filename is None:
        # Auto-generate filename from URL and timestamp
        from datetime import datetime
        from urllib.parse import urlparse
        
        url = driver.current_url
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "").replace(".", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"page_source_code/{domain}_{timestamp}.html"
    
    source = driver.page_source
    
    if include_metadata:
        metadata = f"""<!--
Saved from: {driver.current_url}
Title: {driver.title}
Saved at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
User Agent: {driver.execute_script("return navigator.userAgent;")}
-->
"""
        source = metadata + source
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(source)
    
    print(f"Saved {len(source):,} chars to: {filename}")
    return filename



