from django.test import TestCase
from .models import PersonalInformation
# from .views import MainPage


class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'mainpage.html')

    # def test_save_POST_request(self):
    #     response = self.client.post('/', {'title':'Mr.', 'surname':'Nasam', 
    #         'firstname': 'Bryce', 'email': 'gg@gmail.com', 
    #         'phone': 639478222222})

    #     self.assertEqual(PersonalInformation.objects.count(), 1)

    #     newPersonalInfo = PersonalInformation.objects.first()

    #     self.assertEqual(newPersonalInfo.title, 'Mr.')
    #     self.assertEqual(newPersonalInfo.surname, 'Nasam')
    #     self.assertEqual(newPersonalInfo.firstname, "Bryce")
    #     self.assertEqual(newPersonalInfo.email, 'gg@gmail.com')
    #     self.assertEqual(newPersonalInfo.mobilenumber, 639478222222)
        
    # def test_redirect_POST(self):
    #     response = self.client.post('/',{'title':'Mr.', 'surname':'Nasam', 
    #         'firstname': 'Bryce', 'email': 'gg@gmail.com', 
    #         'phone': 639478222222})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/')


    # def test_only_saves_items_if_necessary(self):
    #     self.client.get('/')
    #     self.assertEqual(PersonalInformation.objects.count(), 0)

#old codes
    # def test_responding_POST_request(self):
    #     resp = self.client.post('/', data={'title': 'newTitle', 'surname': 'newSurname',
    #         'firstname': 'newFirstname','email': 'newEmail', 'phone':'newPhone', 'mail_type':'newMailtype', 'messagetxt': 'newMessage'})
    #     self.assertIn('title', resp.content.decode())
    #     self.assertTemplateUsed(resp,'mainpage.html')

# class ORMTEST(TestCase):
#     def test_saving_retriving(self):
#         samplePersonalInfo = PersonalInformation()
#         samplePersonalInfo.title = 'Ms.'
#         samplePersonalInfo.surname = 'Gadaingan'
#         samplePersonalInfo.firstname = "Samantha"
#         samplePersonalInfo.email = 'samg@gmail.com'
#         samplePersonalInfo.mobilenumber = 639478222222
#         samplePersonalInfo.save()

#         lists = PersonalInformation.objects.all()
#         self.assertEqual(lists.count(), 1)

#         list1 = lists[0]

#         self.assertEqual(list1.title, 'Ms.')
#         self.assertEqual(list1.surname, 'Gadaingan')
#         self.assertEqual(list1.firstname, "Samantha")
#         self.assertEqual(list1.email, 'samg@gmail.com')
#         self.assertEqual(list1.mobilenumber, 639478222222)

#     def test_template_display_list(self):
#         PersonalInformation.objects.create(
#             title='Ms.', 
#             surname='Gadaingan',
#             firstname="Samantha",
#             email='samg@gmail.com',
#             mobilenumber=639478222222)
#         response = self.client.get('/')
#         self.assertIn('1: Ms., Gadaingan, Samantha, samg@gmail.com, 639478222222', 
#             response.content.decode())
#         