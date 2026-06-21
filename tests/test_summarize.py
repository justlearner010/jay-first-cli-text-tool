import pytest
from first_cli.summarize import (
    summarize_text,
    MOCKLLM,
    Summarizer,
    OpenAILLM
)


@pytest.mark.parametrize(
    "text,expected",
    [
        (
            "hello world",
            "Brief summary: this text has 2 words",
        ),
        (
            "你好 世界",
            "Brief summary: this text has 2 words",
        ),
        (
            "",
            "No content to summarize.",
        ),
    ],
)
def test_summarize_brief(text, expected):

    assert summarize_text(text, mode="brief") == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        (
            "hello world",
            [
                "- Word count: 2",
                "- Character count: 11",
                "- Mock summary: this is a placeholder summary.",
            ],
        ),
        (
            "你好 世界",
            [
                "- Word count: 2",
                "- Character count: 5",
                "- Mock summary: this is a placeholder summary.",
            ],
        ),
    ],
)
def test_summarize_bullets(text, expected):
    assert summarize_text(text, mode="bullets") == expected


@pytest.mark.parametrize(
    "mode",
    [
        "unknown",
        "abc",
        "detail",
        "summary",
        "123",
    ],
)
def test_summarize_rejects_unknown_mode(mode):
    with pytest.raises(ValueError):
        summarize_text("hello world", mode=mode)


@pytest.mark.xfail(
    reason="Chinese segmentation is not implemented yet"
)
@pytest.mark.parametrize(
    "text,expected",
    [
        (
            "你好世界",
            "Brief summary: this text has 2 words",
        ),
    ],
)
def test_future_chinese_word_segmentation(text, expected):
    assert summarize_text(text, mode="brief") == expected


def test_mock_llm():
    llm = MOCKLLM()

    result = llm.summarize("hello")

    assert result == "fake summary"


def test_summarizer_uses_llm():
    llm = MOCKLLM()
    summarizer = Summarizer(llm)

    result = summarizer.run("hello")

    assert result == "fake summary"


def test_openai_llm_uses_injected_client():
    class FakeResponse:
        output_text = "fake gpt answer"

    class FakeResponses:
        def create(self, **kwargs):
            self.kwargs = kwargs
            return FakeResponse()

    class FakeClient:
        def __init__(self):
            self.responses = FakeResponses()

    client = FakeClient()
    llm = OpenAILLM(client=client, model="test-model")

    result = llm.summarize("hello")

    assert result == "fake gpt answer"
    assert client.responses.kwargs == {
        "model": "test-model",
        "input": "请总结一下文本:\nhello",
    }
