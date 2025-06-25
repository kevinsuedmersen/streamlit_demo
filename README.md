# Authentication and Authorization
Simple frontend with user authentication and simple FastAPI backend with authorization.

# Prerequisites
## Backend App registration in Azure Portal
Follow the exact steps from this [tutorial](https://intility.github.io/fastapi-azure-auth/single-tenant/azure_setup/). Yes, create two app registrations for the backend. Make sure to add yourself as the owner of these applications!

## Frontend App registration in Azure Portal
Proceed similarly as above. I.e.:
* Register a single tenant application in the azure portal 
* As redirect URI platform select `Single-page application` and enter `http://localhost:8501/` (required by Streamlit for handling user authentication).
* Make sure to add yourself as the owner of this application
* Make sure the `accessTokenAcceptedVersion` in the Manifest is `2`
* Allow the frontend to talk to the backend, i.e. in the `Api Permissions` tab, allow the frontend to use the scope `user_impersonation` defined in the very first app registration.

# Frontend
## Dev setup
If you want to debug the Streamlit frontend and backend from within VS Code, you can use the following run config which must be located at `.vscode/launch.json`:
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "frontend",
            "type": "debugpy",
            "request": "launch",
            "module": "streamlit",
            "cwd": "${workspaceFolder}/frontend",
            "args": [
                "run",
                "1_LOGIN.py",
                "--server.port",
                "8501",
           ],
           "console": "internalConsole"
        },
        {
            "name": "backend",
            "type": "debugpy",
            "request": "launch",
            "cwd": "${workspaceFolder}/backend",
            "program": "src/openapi_server/main.py",
            "console": "internalConsole",
            "env": {
                "PYTHONPATH": "${PYTHONPATH}:/${workspaceFolder}/backend"
            }
        }
    ]
}
```
Note: Initially, this may not work, because Streamlit prompts you to enter your email (which you may leave blank). If that happens start the Streamlit Frontend from the command line using `streamlit run 1_LOGIN.py --server.port 8501` the first time. After that, you can use the above run config. 