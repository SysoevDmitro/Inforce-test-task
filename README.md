# Inforce-test-task
This project for voting for restaurant lunch
## Features
- **JWT**:
  - Authentication with JWT
- **Creating restaurant**
- **Uploading menu for restaurant**
- **Creating employee**
- **Getting current day menu**
- **Getting results  menu for the current day**
- **Dockerized**:
  - Simplified deployment using Docker.
- **API Documentation**:
  - Integrated Swagger documentation.

---
##  How to install

### Using Docker

Follow these steps:

```bash
git clone https://github.com/SysoevDmitro/Inforce-test-task.git
cd Inforce-test-task
docker-compose build
docker-compose up
```
---
## Getting access
- Go to `/api/doc/swagger/` to test api
- Creating user: `/api/user/register/`
- Getting access token: `/api/user/token/`
- Paste access token to `http bearer` in headers
- Test all endpoints
