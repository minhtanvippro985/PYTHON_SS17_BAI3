teams_list = []
match_schedule = []


def input_teams():

    global teams_list, match_schedule
    print("\n--- NHẬP DANH SÁCH ĐỘI TUYỂN ---")
    user_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ").strip()

    if not user_input:
        print("Dữ liệu nhập vào trống!")
        return

    raw_teams = user_input.split(",")
    unique_teams = []
    for team in raw_teams:
        cleaned_team = team.strip().upper()
        if cleaned_team != "" and cleaned_team not in unique_teams:
            unique_teams.append(cleaned_team)

    teams_list = unique_teams
    match_schedule = []  

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")


def create_match_schedule():
    global teams_list, match_schedule
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    tong_so_doi = len(teams_list)
    if tong_so_doi < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return

    match_schedule = []

    index_doi_a = 0
    index_doi_b = 1

    while index_doi_a < tong_so_doi - 1:
        doi_a = teams_list[index_doi_a]
        doi_b = teams_list[index_doi_b]
        match_schedule.append(f"{doi_a} vs {doi_b}")

        index_doi_b += 1

        if index_doi_b == tong_so_doi:
            index_doi_a += 1
            index_doi_b = index_doi_a + 1

    for idx, match in enumerate(match_schedule, 1):
        print(f"{idx}. {match}")

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")
def generate_match_ids():
    global match_schedule
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    for idx, match in enumerate(match_schedule, 1):
        team_parts = match.split(" vs ")
        team_a = team_parts[0]
        team_b = team_parts[1]
        code_a = f"{team_a[0:3]:X<3}"
        code_b = f"{team_b[0:3]:X<3}"
        match_id = f"M{idx:02d}-{code_a}-{code_b}"

        print(f"Trận {idx} ({match}) -> ID: {match_id}")


def main_menu():
    """Giao diện dòng lệnh chính điều hướng toàn bộ hệ thống."""
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Phương pháp cơ bản)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==============================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            input_teams()
        elif choice == "2":
            create_match_schedule()
        elif choice == "3":
            generate_match_ids()
        elif choice == "4":
            print("Hệ thống đang đóng. Tạm biệt!")
            break  
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4.")


if __name__ == "__main__":
    main_menu()