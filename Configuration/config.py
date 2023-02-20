from pydantic import Field, BaseSettings


class DataBaseConfig(BaseSettings):
    HOST: str = Field(env="HOST", default="0.0.0.0", description="Host of the application")
    PORT: int = Field(env="PORT", default=8001, description="Port of the application")
    POSTGRES_USER: str = Field(env="POSTGRES_USER", default="post", description="User name of postgres")
    POSTGRES_PASSWORD: str = Field(env="POSTGRES_PASSWORD", default="password", description="Password of postgres")
    POSTGRES_DB: str = Field(env="POSTGRES_DB", default="db_db", description="Db name of postgres")
    PGADMIN_DEFAULT_EMAIL: str = Field(env="PGADMIN_DEFAULT_EMAIL", default="admin@admin.com", description="PgadminEmail")
    PGADMIN_DEFAULT_PASSWORD: str = Field(env="PGADMIN_DEFAULT_PASSWORD", default="admin", description="PgadminPassword")


config = DataBaseConfig()
