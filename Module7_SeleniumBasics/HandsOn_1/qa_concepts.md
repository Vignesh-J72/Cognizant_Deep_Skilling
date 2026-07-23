Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

Task 1: Map Testing Types to a Real System

1. Testing Types for the Course Management API

 Unit Testing
- Test the `create_course()` function with valid input.
- Expected: Course object is created successfully.
- Type: Functional

Integration Testing
- Send `POST /api/courses/` and verify the database stores the record.
- Expected: HTTP 201 and record exists.
- Type: Functional

System Testing
- Login → Create Course → View → Update → Delete.
- Expected: Entire workflow succeeds.
- Type: Functional

 User Acceptance Testing (UAT)
- College admin creates a course for a semester.
- Expected: Course is available for student enrollment.
- Type: Functional

 Functional vs Non-Functional

| Test | Classification |
|---|---|
| Unit | Functional |
| Integration | Functional |
| System | Functional |
| UAT | Functional |

 Non-Functional Example

Performance Test: 500 concurrent GET `/api/courses/` requests.

Expected:
- Response time < 2 seconds
- No crashes
- Error rate <1%

 Black-Box vs White-Box

| Black-Box | White-Box |
|---|---|
| No knowledge of source code | Internal code is known |
| Tests inputs/outputs | Tests logic and code paths |
| Usually QA | Usually Developers |

 Test Cases

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| TC-001 | Create valid course | API running | POST valid data | HTTP 201 Created |    |    |
| TC-002 | Duplicate course | Course exists | POST same course code | HTTP 409 Conflict |    |    |
| TC-003 | Missing fields | API running | POST without course name | HTTP 400 Bad Request |    |    |

 Task 2: Defect Lifecycle

 Lifecycle

New → Assigned → Open → Fixed → Retest → Verified → Closed

Rejected: Invalid, duplicate or cannot reproduce.

Deferred: Postponed to a future release.

 Severity & Priority

| Bug | Severity | Priority | Justification |
|---|---|---|---|
| POST returns 500 | Critical | P1 | Core feature unusable |
| Long names truncated | Medium | P2 | Data integrity issue |
| Swagger typo | Low | P4 | Cosmetic documentation issue |
| Intermittent 401 login | High | P1 | Unstable authentication |

 Defect Report

| Field | Value |
|---|---|
| Defect ID | BUG-001 |
| Title | POST /api/courses/ returns HTTP 500 |
| Environment | Windows 11, FastAPI |
| Build | v1.0.0 |
| Severity | Critical |
| Priority | P1 |
| Steps | Start API → POST valid course |
| Expected | HTTP 201 Created |
| Actual | HTTP 500 Internal Server Error |
| Attachments | Screenshot of 500 error |

 Severity vs Priority

- Severity: Impact of the defect.
- Priority: Urgency of fixing it.

Example: XML export crashes.
- Severity: High
- Priority: Low (rarely used feature)
