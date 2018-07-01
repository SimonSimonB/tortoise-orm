from tortoise.contrib.testing import TestCase
from tortoise.tests.testmodels import Tournament


class TestBasic(TestCase):
    async def test_basic(self):
        event = await Tournament.create(name='Test')
        await Tournament.filter(id=event.id).update(name='Updated name')
        saved_event = await Tournament.filter(name='Updated name').first()
        self.assertEquals(saved_event.id, event.id)
        await Tournament(name='Test 2').save()
        self.assertEquals(
            await Tournament.all().values_list('id', flat=True),
            [1, 2]
        )
        self.assertEquals(
            await Tournament.all().values('id', 'name'),
            [{'id': 1, 'name': 'Updated name'}, {'id': 2, 'name': 'Test 2'}]
        )
