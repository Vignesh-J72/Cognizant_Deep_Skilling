 Hands-On 2: SDLC vs TDLC – V-Model & Agile QA Integration

 Task 1: V-Model Mapping

 9. V-Model Diagram

text
                    SDLC (Development)

Requirements
      │
      ▼
System Design
      │
      ▼
Architecture Design
      │
      ▼
Module Design
      │
      ▼
    Coding
      ▲
      │
Unit Testing
      ▲
      │
Integration Testing
      ▲
      │
System Testing
      ▲
      │
Acceptance Testing

               TDLC (Testing)


 10. SDLC ↔ TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements Analysis | Acceptance Testing | Acceptance Test Plan, Acceptance Test Cases |
| System Design | System Testing | System Test Plan and Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan and Interface Test Cases |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Execution of Tests | Source Code and Build |

---

 11. Entry and Exit Criteria

 Unit Testing

Entry Criteria
- Module coding completed.
- Source code reviewed.
- Development environment is ready.

Exit Criteria
- All unit test cases executed.
- 100% critical test cases passed.
- No open critical defects.

---

 Integration Testing

Entry Criteria
- Individual modules have passed unit testing.
- Interfaces are available.
- Integration environment is ready.

Exit Criteria
- All integration test cases executed.
- Module interactions work correctly.
- No critical integration defects remain.

---

 System Testing

Entry Criteria
- Entire application is integrated.
- Test environment is configured.
- Test data is prepared.

Exit Criteria
- Functional and regression testing completed.
- No open Critical or High severity defects.
- Test summary report prepared.

---

 Acceptance Testing

Entry Criteria
- System testing completed successfully.
- Business users are available.
- Acceptance test scenarios prepared.

Exit Criteria
- Customer approves the application.
- All acceptance criteria satisfied.
- Product is ready for deployment.

---

 12. QA Engagement During the Course Management API Project

QA should participate before testing begins.

 1. Requirements Review

- Review functional requirements.
- Identify ambiguities.
- Define acceptance criteria.
- Ensure requirements are testable.

 2. Design Review

- Review API endpoints.
- Verify validation rules.
- Check database relationships.
- Identify potential testing risks early.

Early QA involvement reduces defects and lowers development cost.

---

 Task 2: Agile QA and Shift-Left Testing

 13. Problems with Waterfall Testing

Testing only after development causes several issues.

Problem 1
Defects are discovered late, making them expensive to fix.

Problem 2
Requirement changes become difficult because development is already complete.

Problem 3
Customers receive feedback very late, increasing the risk of building the wrong product.

---

 14. QA Responsibilities in Agile

| Agile Ceremony | QA Responsibility |
|---------------|-------------------|
| Sprint Planning | Review user stories, estimate testing effort, define acceptance criteria |
| Daily Stand-up | Report testing progress, discuss blockers, coordinate with developers |
| Sprint Review | Validate completed features and demonstrate tested functionality |
| Retrospective | Discuss issues faced during testing and suggest process improvements |

---

 15. Shift-Left Practices

 a) Review Requirements for Testability

QA reviews requirements before development begins to remove ambiguity and ensure every requirement can be tested.

 b) Write Test Cases Before Coding (TDD/BDD)

QA prepares test scenarios and acceptance criteria before implementation so developers clearly understand expected behavior.

 c) Static Code Analysis

Developers use static analysis tools to detect coding issues, security vulnerabilities, and code quality problems before execution.

 d) API Contract Testing

Verify API request and response formats before integrating frontend and backend components to detect interface issues early.

---

 16. Acceptance Criteria (Given–When–Then)

Scenario 1: Successful Course Creation


Given the college admin is logged into the system
When valid course details are submitted
Then the course should be created successfully
And the API should return HTTP 201 Created


Scenario 2: Duplicate Course Code


Given a course with code "CS101" already exists
When the admin submits another course with the same code
Then the API should return HTTP 409 Conflict
And an error message should indicate that the course code already exists


Scenario 3: Missing Required Fields


Given the college admin is logged into the system
When the course name or course code is missing
Then the API should return HTTP 400 Bad Request
And validation errors should be displayed

