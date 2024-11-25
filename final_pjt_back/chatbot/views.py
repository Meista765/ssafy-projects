from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import openai

# Create your views here.


@api_view(["POST"])
def chat_with_gpt(request):
    try:
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

        messages = request.data.get("messages", [])

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0,
            top_p=1,
        )

        return Response({"message": response.choices[0].message.content})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
