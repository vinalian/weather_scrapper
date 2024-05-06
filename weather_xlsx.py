import argparse
from xlsx_scripts.xlsx_main import create_xlsx


async def main():
    parser = argparse.ArgumentParser(description="Generate Excel file with weather data")
    parser.add_argument("--filename", "-f", type=str, required=True, help="Output filename (must end with .xlsx)")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Number of records to fetch from the database (default: 10)")
    args = parser.parse_args()

    await create_xlsx(limit=args.limit)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
