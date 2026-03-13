from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def api_root(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CryptoSphere | Professional API</title>
        <style>
            body { font-family: 'Inter', -apple-system, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: #1e293b; padding: 3rem; border-radius: 1rem; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); border: 1px solid #334155; max-width: 600px; width: 90%; }
            .badge { background: #38bdf8; color: #0f172a; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.875rem; font-weight: bold; text-transform: uppercase; }
            h1 { font-size: 2.5rem; margin: 1.5rem 0 0.5rem; color: #fff; }
            p { color: #94a3b8; line-height: 1.6; font-size: 1.1rem; }
            .endpoints { margin-top: 2rem; background: #0f172a; padding: 1.5rem; border-radius: 0.5rem; border-left: 4px solid #38bdf8; }
            code { color: #38bdf8; font-family: 'Fira Code', monospace; }
            .footer { margin-top: 2rem; font-size: 0.875rem; color: #64748b; border-top: 1px solid #334155; padding-top: 1.5rem; }
            a { color: #38bdf8; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">v1.0.0 Live</span>
            <h1>CryptoSphere Core</h1>
            <p>High-performance backend engine for real-time cryptocurrency price tracking and automated alerting systems.</p>

            <div class="endpoints">
                <strong>Main Endpoints:</strong><br><br>
                <code>GET / </code> - API Health Check (Current)<br>
                <code>GET /admin/ </code> - Management Dashboard<br>
            </div>

            <div class="footer">
                Status: <span style="color: #22c55e;">● Operational</span> | 
                System: <strong>Django 5.0 + PostgreSQL</strong> | 
                <a href="/admin/">Enter Dashboard →</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
]