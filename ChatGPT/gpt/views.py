from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import openai

class TextGenerationAPIView(APIView):
    def post(self, request):
        openai.api_key = "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"
        prompt = request.POST.get("prompt", "")
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2000,
            n=2,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return Response({"message": message})

def generate_text(request):
    if request.method == "POST":
        text = TextGenerationAPIView().post(request).data.get("message")
        return render(request, "generated_text.html", {"text": text})
    return render(request, "generate_text.html")


class GenerationEngineListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        engines = [
            {
                "name": "davinci",
                "description": "High-fidelity language model with access to the web's information.",
                "features": [
                    "large-scale language understanding",
                    "state-of-the-art generation quality",
                    "integration with the web's information"
                ]
            },
            {
                "name": "curie",
                "description": "Lower-cost language model with a more limited scope of knowledge.",
                "features": [
                    "fast response time",
                    "lower cost than davinci",
                    "specialized knowledge in a smaller range of topics"
                ]
            },
            {
                "name": "babbage",
                "description": "High-speed language model optimized for answering questions.",
                "features": [
                    "fast response time",
                    "specialized knowledge in answering questions",
                    "knowledge from a smaller range of sources"
                ]
            }
        ]
        return Response(engines)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# import openai

# class AllGenerationEngineAPI(APIView):
#     def post(self, request):
#         # Extract the request data
#         engine = request.data.get('engine')
#         prompt = request.data.get('prompt')
#         max_tokens = request.data.get('max_tokens', 2000)
#         stop = request.data.get('stop', None)

#         # Validate the request data
#         if engine is None or prompt is None:
#             return Response({'error': 'Engine and prompt are required fields'}, status=status.HTTP_400_BAD_REQUEST)

#         # Use the OpenAI API to generate text
#         completions = openai.Completion.create(
#             engine=engine,
#             prompt=prompt,
#             max_tokens=max_tokens,
#             stop=stop,
#             n=1,
#             temperature=0.5,
#         )
#         message = completions.choices[0].text
#         return Response({'text': message})
