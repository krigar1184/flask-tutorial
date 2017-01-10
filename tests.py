#!venv/bin/python

import os
import unittest
from datetime import datetime, timedelta
from config import basedir
from app import app, db
from app.models import User, Post


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_avatar(self):
        u = User(nickname='john', email='john@example.com')
        avatar = u.avatar(128)
        expected = 'http://gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=mm&s=128'
        self.assertEqual(avatar[0:len(expected)], expected)

    def test_make_unique_nickname(self):
        u = User(nickname='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()

        nickname = User.make_unique_nickname('john')
        self.assertNotEqual('john', nickname)

        u2 = User(nickname=nickname, email='susan@example.com')
        db.session.add(u2)
        db.session.commit()

        nickname2 = User.make_unique_nickname('john')
        self.assertNotEqual(nickname2, 'john')
        self.assertNotEqual(nickname2, nickname)

    def test_follow(self):
        u1 = User(nickname='john', email='john@example.com')
        u2 = User(nickname='susan', email='susan@example.com')

        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        self.assertEqual(2, User.query.count())

        u = u1.follow(u2)
        db.session.add(u)
        db.session.commit()

        self.assertEqual(u2.followers.count(), 1)
        self.assertTrue(u1.is_following(u2))
        self.assertFalse(u2.is_following(u1))

        u = u1.unfollow(u2)
        db.session.add(u)
        db.session.commit()

        self.assertEqual(0, u2.followers.count())
        self.assertEqual(0, u1.followed.count())
        self.assertFalse(u1.is_following(u2))

    def test_follow_posts(self):
        u1 = User(nickname='john', email='john@example.com')
        u2 = User(nickname='susan', email='susan@example.com')
        u3 = User(nickname='alice', email='alice@example.com')
        u4 = User(nickname='bob', email='bob@example.com')

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        db.session.commit()

        utcnow = datetime.utcnow()
        p1 = Post(body='post from John', author=u1, timestamp=utcnow + timedelta(seconds=1))
        p2 = Post(body='post from Susan', author=u2, timestamp=utcnow + timedelta(seconds=2))
        p3 = Post(body='post from Alice', author=u3, timestamp=utcnow + timedelta(seconds=3))
        p4 = Post(body='post from Bob', author=u4, timestamp=utcnow + timedelta(seconds=4))

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()

        u1.follow(u1)
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u2)
        u2.follow(u3)
        u3.follow(u3)
        u3.follow(u4)
        u4.follow(u4)

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        db.session.commit()

        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()

        self.assertEqual(3, len(f1))
        self.assertEqual(2, len(f2))
        self.assertEqual(2, len(f3))
        self.assertEqual(1, len(f4))
        self.assertEqual(f1, [p4, p2, p1])
        self.assertEqual(f2, [p3, p2])
        self.assertEqual(f3, [p4, p3])
        self.assertEqual(f4, [p4])
if __name__ == '__main__':
    unittest.main()
