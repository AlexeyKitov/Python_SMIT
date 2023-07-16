from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "costofinsurance" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "actual_date" DATE NOT NULL,
    "cargo" VARCHAR(50) NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    CONSTRAINT "uid_costofinsur_actual__c67b48" UNIQUE ("actual_date", "cargo")
);
COMMENT ON TABLE "costofinsurance" IS 'Модель стоимости страховки';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
