class Config:
    SQLALCHEMY_DATABASE_URI = 'cockroachdb://ivan_robin_epitech_d:-i1IHUTawzA4L7vTCpwPCw@optical3-10083.j77.aws-eu-central-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full'  # Example DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
