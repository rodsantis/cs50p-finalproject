from unittest.mock import patch
from pytest import mark
from project import game_info, get_director, get_actor


data = [[{'title': 'Voices from Mariel'}, {'released': 2011}], [{'name': 'James Carleton'}],
        [{'name': 'Steven Bauer'}], [{'rating': 9.2}, {'votes': 10}]]


@patch('project.get_movie.main')
def test_game_info(mock_get):
    """ Testing the return of 4 values as our game needs 4 values return to function"""
    mock_get.return_value = ['a', 'b', 'c', 'd']
    assert game_info() == ['a', 'b', 'c', 'd']


def test_get_director():
    data = [[{'title': 'Voices from Mariel'}, {'released': 2011}], [{'name': 'James Carleton'}],
            [{'name': 'Steven Bauer'}], [{'rating': 9.2}, {'votes': 10}]]
    assert get_director(data) == "James Carleton"


@mark.parametrize(
    "raw_data, expected_value",
    [
        (
            [[{'title': 'Voices from Mariel'}, {'released': 2011}], [{'name': 'James Carleton'}],
            [{'name': 'Steven Bauer'}], [{'rating': 9.2}, {'votes': 10}]],
            "Steven Bauer"
        ),
        (
                [[{'title': 'Ishq Nachavye Gali Gali'}, {'released': 1996}], [{'name': 'Balwant Dullat'}, {'name': 'Ishwar Singh'}], [{'name': 'Manjeet Kular'}, {'name': 'Shavinder Mahal'}, {'name': 'Deepak Saraf'}, {'name': 'Singh Neeru'}], [{'rating': 4.2}, {'votes': 16}]],
                "Manjeet Kular, Shavinder Mahal, Deepak Saraf, Singh Neeru"
        )
    ]
)
def test_get_actor(raw_data, expected_value):
    assert get_actor(raw_data) == expected_value


if __name__ == "__main__":
    main()