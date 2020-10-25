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

if __name__=="__main__":
    unittest.main()

