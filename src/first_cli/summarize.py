class OpenAILLM:
    def __init__(self, client=None, model="gpt-5.5"):
        self.client = client
        self.model = model

    def _get_client(self):
        if self.client is None:
            try:
                from openai import OpenAI
            except ModuleNotFoundError as exc:
                raise RuntimeError(
                    "OpenAI SDK is not installed. Install it before using OpenAILLM."
                ) from exc

            self.client = OpenAI()

        return self.client

    def summarize(self, text):
        client = self._get_client()
        response = client.responses.create(
            model=self.model,
            input=f"请总结一下文本:\n{text}"
        )

        return response.output_text


class MOCKLLM:
    def summarize(self, text):
        return "fake summary"


class Summarizer:

    def __init__(self, llm):
        self.llm = llm

    def run(self, text):
        if not text.strip():
            return "No content to summarize."

        return self.llm.summarize(text)


def summarize_text(text, mode="brief"):

    if not text.strip():
        return "No content to summarize."

    if mode == "brief":
        return f"Brief summary: this text has {len(text.split())} words"

    if mode == "bullets":
        return [
            f"- Word count: {len(text.split())}",
            f"- Character count: {len(text)}",
            "- Mock summary: this is a placeholder summary.",
        ]

    raise ValueError("mode must be 'brief' or 'bullets'")
