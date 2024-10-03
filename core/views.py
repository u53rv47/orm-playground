import logging

from django.shortcuts import render
from django.http.response import JsonResponse

from core.models import Question, Answer, Solution


logger = logging.getLogger("core")


# Create your views here.
def index(request):
    """Render main page"""
    databases = [
        {"value": "IN", "name": "Inventory"},
    ]
    languages = [
        {"value": "sql", "name": "SQL"},
        {"value": "python", "name": "Python"},
        {"value": "java", "name": "Java"},
        {"value": "javascript", "name": "JavaScript"},
    ]
    frameworks = {
        "python": [
            {"value": "django", "name": "Django"},
            {"value": "sqlalchemy", "name": "SQLAlchemy"},
        ],
        "java": [
            {"value": "hibernate", "name": "Hibernate"},
            {"value": "spring", "name": "Spring"},
        ],
        "javascript": [{"value": "prisma", "name": "Prisma"}],
    }
    return render(
        request,
        "core/index.html",
        {"databases": databases, "languages": languages, "frameworks": frameworks},
    )


def get_all_questions(request, database):
    """Get all the questions of a database"""

    questions = Question.objects.filter(database=database)
    question_list = list(questions.values("q_no", "q_text"))

    logger.info(question_list)
    return JsonResponse(question_list, safe=False)
