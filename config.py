import os


class Config:
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ENVIRON_KEY = os.environ.get("CI_TEST_KEY", "the key is missing")


class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = "postgresql:///ci_test"


class TestConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "postgresql:///ci_test_test"


environments = {
	"dev" : DevelopmentConfig,
	"test" : TestConfig,
}
