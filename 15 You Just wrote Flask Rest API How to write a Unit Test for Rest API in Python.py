try:
    from run import app
    import unittest
except Exception as e:
    print("Some Modules are Missing{}".format(e))

class FlaskTest(unittest.TestCase):

    #Check for response 200
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get("/fo")
        satuscode=response.status_code
        self.assertEqual(satuscode,200)

    # check if the content return is application?json
    def test_index_content(self):
        tester=app.text_client(self)
        response=tester.get("/fo")
        self.assertEqual(response.content_type,"application/json")

    # check for DAta returned
    def test_index_data(self):
        tester=app.test_client(self)
        response=tester.get("/fo")
        self.assertTrue(b'Message' in response.data)


if __name__=="__main__":
    unittest.main()

