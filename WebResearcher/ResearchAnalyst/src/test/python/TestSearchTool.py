import unittest
from unittest.mock import patch, MagicMock
from tools.search_tool import SearchTool


class TestSearchTool(unittest.TestCase):

    @patch('my_module.TavilyClient')
    def test_run_method(self, mock_tavily_client):
        # Set up the test data
        test_argument = "test query"

        # Mock the behavior of TavilyClient
        mock_client_instance = MagicMock()
        mock_client_instance.search.return_value = "test response"
        mock_tavily_client.return_value = mock_client_instance

        # Instantiate SearchTool
        search_tool = SearchTool()

        # Call the _run method
        result = search_tool._run(test_argument)

        # Assert that TavilyClient.search was called with the correct argument
        mock_client_instance.search.assert_called_once_with(query=test_argument)

        # Assert that the result is not None
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
