from django.http import HttpResponse


def api_root(request):
    """
    Main entry point for the CryptoSphere API.
    Fixed active links for seamless navigation.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CryptoSphere | Professional API</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Inter', sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: #1e293b; padding: 3rem; border-radius: 1rem; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); border: 1px solid #334155; max-width: 600px; width: 90%; }
            .badge { background: #38bdf8; color: #0f172a; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem; font-weight: bold; text-transform: uppercase; }
            h1 { font-size: 2.5rem; margin: 1.5rem 0 0.5rem; color: #fff; }
            p { color: #94a3b8; line-height: 1.6; font-size: 1.1rem; }
            .endpoints { margin-top: 2rem; background: #0f172a; padding: 1.5rem; border-radius: 0.5rem; border-left: 4px solid #38bdf8; }
            code { color: #38bdf8; font-family: 'Fira Code', monospace; font-size: 0.95rem; }
            .endpoint-link { display: block; margin-bottom: 10px; text-decoration: none; transition: 0.2s; }
            .endpoint-link:hover code { background: #1e293b; color: #7dd3fc; }
            .footer { margin-top: 2rem; font-size: 0.875rem; color: #64748b; border-top: 1px solid #334155; padding-top: 1.5rem; }
            .status-dot { color: #22c55e; margin-right: 5px; }
            a { color: #38bdf8; text-decoration: none; font-weight: 600; }
            a:hover { text-decoration: underline; }
            .main-btn { display: inline-block; margin-top: 10px; background: #38bdf8; color: #0f172a; padding: 0.6rem 1.2rem; border-radius: 0.5rem; font-weight: bold; transition: 0.3s; }
            .main-btn:hover { background: #7dd3fc; transform: translateY(-2px); text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">v1.0.0 Live</span>
            <h1>CryptoSphere Core</h1>
            <p>High-performance backend engine for real-time cryptocurrency price tracking and automated alerting systems.</p>

            <div class="endpoints">
                <strong>Main API Endpoints:</strong><br><br>
                <a href="/api/alerts/" class="endpoint-link"><code>GET /api/alerts/ </code></a>
                <a href="/api/docs/" class="endpoint-link"><code>GET /api/docs/   </code></a>
                <a href="/admin/" class="endpoint-link"><code>GET /admin/      </code></a>
            </div>

            <div class="footer">
                Status: <span class="status-dot">●</span>Operational | 
                Core: <strong>Django REST Framework</strong> | <br><br>
                <a href="/api/docs/" class="main-btn">Explore API Documentation →</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
