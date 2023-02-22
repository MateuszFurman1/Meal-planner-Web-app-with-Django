from django.core.management.base import BaseCommand
from jedzonko.factories import RecipeFactory, PlanFactory, RecipePlanFactory, PageFactory, DayNameFactory
from django.db import transaction


class Command(BaseCommand):
    help = 'Seeds the database with dummy data'

    def handle(self, *args, **options):
        with transaction.atomic():
            days = ('Poniedziałek', 'Wtorek', 'Środa',
                    'Czwartek', 'Piątek', 'Sobota', 'Niedziela')
            recipe_names = ('ŁOSOŚ TERIYAKI PIECZONY NA RYŻU', 'FILETY DROBIOWE PANKO W SOSIE POMIDOROWYM Z CIECIERZYCĄ',
                            'DORSZ Z PORAMI', 'PSTRĄG Z PIEKARNIKA', 'MAKARON PRIMAVERA Z KURCZAKIEM',
                            'DORSZ W SOSIE CURRY', 'KURCZAK W SOSIE CURRY')
            plan_names = ('Sport', 'Slim', 'FodMap', 'Keto',
                          'Low Carb', 'Low IG', 'Wege')
            page = PageFactory()
            for i in range(0, 7):
                day = DayNameFactory(name=days[i])
                recipe = RecipeFactory(name=recipe_names[i])
                plan = PlanFactory(name=plan_names[i])
                recipe_plan = RecipePlanFactory(
                    recipe=recipe, plan=plan, day=day)
