import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)


def calculate_actual_pay(player):
    """Tính lương thực nhận"""

    if player["status"] == "Benched":
        return player["salary"] * 0.5

    return player["salary"]


def display_roster(roster_list):
    """Hiển thị đội hình"""

    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    logging.info("Coach viewed the team roster.")

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")

    for player in roster_list:

        status = player.get("status", "Unknown")

        name = player["name"]

        if status == "Benched":
            name += " [DỰ BỊ]"

        print(
            f"{player['player_id']} | "
            f"{name} | "
            f"{player['role']} | "
            f"{player['salary']} | "
            f"{status}"
        )


def sign_player(roster_list):
    """Chiêu mộ tuyển thủ"""

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    for player in roster_list:
        if player["player_id"] == player_id:
            print("Mã tuyển thủ đã tồn tại.")
            logging.warning(
                f"Duplicate player ID {player_id}"
            )
            return

    name = input("Tên: ")
    role = input("Vị trí: ")

    while True:
        try:
            salary = float(input("Lương: "))

            if salary <= 0:
                print("Lương phải > 0")
                continue

            break

        except ValueError:
            print("Lương phải là số.")
            logging.warning(
                "Invalid salary input"
            )

    roster_list.append(
        {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": "Active"
        }
    )

    logging.info(
        f"Signed new player {name}"
    )


def generate_payroll_report(roster_list):
    """Báo cáo quỹ lương"""

    total = 0

    for player in roster_list:

        try:
            actual_pay = calculate_actual_pay(player)

            total += actual_pay

        except KeyError as error:
            print(
                "Lỗi: Một tuyển thủ đang bị thiếu dữ liệu."
            )

            logging.error(
                f"Missing key: {error}"
            )

    print(f"Tổng quỹ lương: {total}")