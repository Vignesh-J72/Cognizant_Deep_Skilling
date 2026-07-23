 Hands-On 3: Test Automation Process, Lifecycle & Framework Types

 Task 1: Automation Decision and Test Case Selection

 1. Criteria for Automation

| Criterion | Explanation | Applied to POST /api/courses/ |
|---|---|---|
| Repetitive | Tests executed frequently | Suitable for automation |
| Stable | Functionality changes rarely | Suitable |
| High Risk | Failure impacts users | Suitable |
| Data-Driven | Multiple inputs required | Suitable |
| Time Saving | Reduces manual effort | Suitable |

 2. Automate or Manual?

| Test Case | Decision | Justification |
|---|---|---|
| CRUD regression after every change | Automate | Frequent regression testing |
| Exploratory testing | Manual | Requires human judgment |
| Performance test (100 users) | Automate | Tool-based execution |
| Login UI test | Automate | Frequently executed |
| Swagger documentation verification | Manual | Mostly visual review |
| Smoke test after deployment | Automate | Quick deployment validation |

 3. Test Automation ROI

Definition

Return on Investment (ROI) measures whether the time and cost spent creating automation are recovered through repeated execution.

- Automation development: 4 hours
- Manual execution: 30 minutes (0.5 hours)

Break-even:

4 ÷ 0.5 = 8 runs

After the 10th run, maintenance overhead:

20% × 0.5 = 0.1 hour

Automated execution remains significantly cheaper than manual execution, so ROI continues to increase over time.

 4. Flaky Tests

A flaky test produces inconsistent results without changes in the application.

Example

A Selenium login test occasionally fails because the page has not finished loading.

Prevention
1. Use explicit waits instead of fixed delays.
2. Avoid unstable locators; use unique IDs.
3. Reset test data before every execution.

---

Task 2: Framework Types

1. Framework Comparison

 Linear Framework
Description: Test scripts are executed sequentially with little or no reuse.

Advantage: Simple to develop.

Disadvantage: Difficult to maintain.

Course Management Example: Small proof-of-concept project.


 Modular Framework

Description: Application is divided into reusable modules.

Advantage: Code reuse.

Disadvantage: Initial design requires planning.

Example: Separate login, courses, and students modules.



Data-Driven Framework

Description: Test data is stored separately from scripts.

Advantage: One script tests many datasets.

Disadvantage: Managing large datasets.

Example: Login with 50 username/password combinations.



Keyword-Driven Framework

Description: Tests are written using keywords representing actions.

Advantage: Non-technical testers can contribute.

Disadvantage: Higher implementation complexity.

Example: Keywords such as Login, ClickButton, VerifyMessage.



 Hybrid Framework

Description: Combines Modular, Data-Driven and Keyword-Driven approaches.

Advantage: Flexible, scalable and reusable.

Disadvantage: More complex to design.

Example: Enterprise Course Management testing suite.



 2. Recommended Framework

Recommendation: Hybrid Framework

 Justification

- Modular design allows reuse of login functionality.
- Data-driven testing supports 50 login combinations.
- Keyword-driven layer enables non-technical testers.
- Suitable for large Selenium automation projects.



 3. Hybrid Framework Folder Structure

text
CourseManagementAutomation/
│
├── config/
│   ├── config.properties
│   └── environment.properties
│
├── testdata/
│   ├── login_data.xlsx
│   └── courses.json
│
├── pages/
│   ├── LoginPage.py
│   ├── DashboardPage.py
│   └── CoursePage.py
│
├── tests/
│   ├── test_login.py
│   ├── test_courses.py
│   └── test_smoke.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   └── helpers.py
│
├── keywords/
│   ├── login_keywords.py
│   └── course_keywords.py
│
├── reports/
│
└── screenshots/


