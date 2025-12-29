from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Pushups workout', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Running workout', difficulty='Medium')

        # Create activities
        Activity.objects.create(user=users[0], workout=pushups, date=timezone.now().date(), duration=30, notes='Morning pushups')
        Activity.objects.create(user=users[1], workout=running, date=timezone.now().date(), duration=45, notes='Evening run')
        Activity.objects.create(user=users[2], workout=pushups, date=timezone.now().date(), duration=20, notes='Quick set')
        Activity.objects.create(user=users[3], workout=running, date=timezone.now().date(), duration=60, notes='Night run')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=75)
        Leaderboard.objects.create(team=dc, total_points=80)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
