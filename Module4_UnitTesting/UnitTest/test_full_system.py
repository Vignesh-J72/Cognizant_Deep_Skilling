import unittest
from unittest.mock import MagicMock, patch

class NotificationService:
    def send_email_alert(self, employee_id, cert_name):
        pass

class CertificationManager:
    def __init__(self, notification_service):
        self.notification_service = notification_service
        self.certifications=[]

    def add_certification(self, cert_name, validity_years):
        if validity_years<=0:
            raise ValueError("Validity period must be greater than 0 years")
        self.certifications.append({"name": cert_name, "validity": validity_years})

    def get_total_certs(self):
        return len(self.certifications)

    def issue_certification(self, employee_id, cert_name, validity_years):
        self.add_certification(cert_name, validity_years)
        return self.notification_service.send_email_alert(employee_id, cert_name)

class TestCertificationManager(unittest.TestCase):

    def setUp(self):
        self.mock_notifier=MagicMock()
        self.manager=CertificationManager(self.mock_notifier)

    def tearDown(self):
        self.manager.certifications.clear()

    def test_add_certification_and_count(self):
        self.manager.add_certification("AWS Solutions Architect", 3)
        self.manager.add_certification("Certified Scrum Master", 2)
        
        self.assertEqual(self.manager.get_total_certs(), 2)
        self.assertIn({"name":"AWS Solutions Architect","validity": 3}, self.manager.certifications)

    def test_invalid_validity_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_certification("Expired Token Cert", 0)

    @patch('__main__.NotificationService.send_email_alert')
    def test_issuing_cert_triggers_email_notification(self, mock_send_alert):
        mock_send_alert.return_value="STATUS_SENT_200"
        manager_with_patched_service=CertificationManager(NotificationService())
        result=manager_with_patched_service.issue_certification(
            employee_id="EMP104", 
            cert_name="Google Cloud Professional", 
            validity_years=2
        )
        
        self.assertEqual(result, "STATUS_SENT_200")
        mock_send_alert.assert_called_once_with("EMP104", "Google Cloud Professional")


def employee_cert_suite():
    suite=unittest.TestSuite()
    suite.addTest(TestCertificationManager('test_add_certification_and_count'))
    suite.addTest(TestCertificationManager('test_invalid_validity_raises_error'))
    return suite


if __name__ == '__main__':
    unittest.main()
    
    