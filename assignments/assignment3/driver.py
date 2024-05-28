# Towa Quimbayo, A01086002
# Noufil Saqib, A01167801

import asyncio
import platform
from pokedex_facade import PokedexFacade


async def main():
    try:
        request = PokedexFacade.get_request_from_args()
        response = await PokedexFacade().execute_request(request)
        PokedexFacade.create_report(response, request.output_type)
    except ValueError as e:
        print(f"ValueError: {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
