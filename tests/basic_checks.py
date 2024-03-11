import unittest
import os
import importlib.util

class TestLLMModelCascade(unittest.TestCase):

    def test_library_langchain_installed(self):
        """ Test if langchain library is installed """
        langchain_installed = importlib.util.find_spec("langchain") is not None
        self.assertTrue(langchain_installed, "langchain library is not installed")

    def test_library_ipywidgets_installed(self):
        """ Test if ipywidgets library is installed """
        ipywidgets_installed = importlib.util.find_spec("ipywidgets") is not None
        self.assertTrue(ipywidgets_installed, "ipywidgets library is not installed")

    def test_library_langchain_openai_installed(self):
        """ Test if langchain-openai library is installed """
        langchain_openai_installed = importlib.util.find_spec("langchain_openai") is not None
        self.assertTrue(langchain_openai_installed, "langchain-openai library is not installed")
      
    def test_library_langchain_experimental_installed(self):
        """ Test if langchain-experimental library is installed """
        langchain_experimental_installed = importlib.util.find_spec("langchain_experimental") is not None
        self.assertTrue(langchain_experimental_installed, "langchain-experimental library is not installed")
      
    def test_library_sentence_transformers_installed(self):
        """ Test if sentence-transformers library is installed """
        sentence_transformers_installed = importlib.util.find_spec("sentence_transformers") is not None
        self.assertTrue(sentence_transformers_installed, "sentence-transformers library is not installed")

if __name__ == '__main__':
    unittest.main()
