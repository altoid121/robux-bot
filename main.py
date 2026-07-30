import discord
from discord.ext import commands

# 봇 초기화
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# 관리자 ID 설정
admin_id = 1342827283341246526  # 관리자 ID를 여기에 넣으세요

# 환율 설정 및 계산을 위한 변수
rate_per_won = 667  # 1만원에 몇 로벅스를 설정할지

# 슬래시 커맨드 동기화
@bot.event
async def on_ready():
    # 슬래시 커맨드 동기화
    await bot.tree.sync()
    print(f'{bot.user} is ready and commands are synced!')

# 환율 설정 명령어 (관리자만 사용 가능)
@bot.tree.command(name="가격설정", description="1만원에 몇 로벅스를 설정할지 입력합니다.")
async def 가격설정(interaction: discord.Interaction, rate: float):
    if interaction.user.id != admin_id:  # 관리자만 사용할 수 있도록 설정
        await interaction.response.send_message("이 명령어는 관리자만 사용할 수 있습니다.", ephemeral=True)
        return

    global rate_per_won
    rate_per_won = rate
    await interaction.response.send_message(f"1만원에 {rate} 로벅스를 설정했습니다.", ephemeral=True)

# 환율 계산 명령어
@bot.tree.command(name="계산", description="입력한 금액을 로벅스로 계산합니다.")
async def 계산(interaction: discord.Interaction, amount: float):
    if rate_per_won is None:
        await interaction.response.send_message("먼저 가격설정 명령어로 환율을 설정해주세요.", ephemeral=True)
        return

    # 계산: amount (원) -> 로벅스로 변환
    robux_amount = (amount / 10000) * rate_per_won
    await interaction.response.send_message(f"{amount} 원은 {robux_amount} 로벅스입니다.", ephemeral=True)

# 봇 실행
bot.run("MTUzMjMzMDQ0MDA0Mjc0MTg1Mg.GDEoSN.v4cat6_ISbR3hMapmOH4CyhTB5ZDGWzRToHvWg")