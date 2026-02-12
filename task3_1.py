class BankError(Exception):
    pass
    
class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = {}

class BankAccount:
    def __init__(self, account_number, currency, client_id):
        self.account_number = account_number
        self.currency = currency
        self.balance = 0.0
        self.client_id = client_id

class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}
        self.next_account_number = 1
    
    def create_client(self, client_id, name):
        try:
            if client_id in self.clients:
                return "Ошибка: Клиент с таким ID уже существует"
            
            self.clients[client_id] = Client(client_id, name)
            return f"Клиент {name} создан"
        except BankError as b:
            return f"Ошибка при создании клиента: {b}"
    
    def open_account(self, client_id, currency):
        try:
            if client_id not in self.clients:
                return "Ошибка: Клиент не найден"
            
            client = self.clients[client_id]
            if currency in client.accounts:
                return f"Ошибка: У клиента уже есть счет в валюте {currency}"
            
            account_number = f"ACC{self.next_account_number:06d}"
            account = BankAccount(account_number, currency, client_id)
            
            self.accounts[account_number] = account
            client.accounts[currency] = account
            self.next_account_number += 1
            
            return f"Счет {account_number} открыт"
        except BankError as b:
            return f"Ошибка при открытии счета: {b}"
    
    def close_account(self, client_id, account_number):
        try:
            if account_number not in self.accounts:
                return "Ошибка: Счет не найден"
            
            account = self.accounts[account_number]
            if account.client_id != client_id:
                return "Ошибка: Недостаточно прав для закрытия счета"
            
            if account.balance != 0:
                return "Ошибка: Нельзя закрыть счет с ненулевым балансом"
            
            client = self.clients[client_id]
            del client.accounts[account.currency]
            del self.accounts[account_number]
            
            return "Счет закрыт"
        except BankError as b:
            return f"Ошибка при закрытии счета: {b}"
    
    def deposit(self, account_number, amount):
        try:
            if amount <= 0:
                return "Ошибка: Сумма должна быть положительной"
            
            account = self.accounts.get(account_number)
            if not account:
                return "Ошибка: Счет не найден"
            
            account.balance += amount
            return f"Счет пополнен на {amount}. Новый баланс: {account.balance}"
        except BankError as b:
            return f"Ошибка при пополнении счета: {b}"
    
    def withdraw(self, account_number, amount):
        try:
            if amount <= 0:
                return "Ошибка: Сумма должна быть положительной"
            
            account = self.accounts.get(account_number)
            if not account:
                return "Ошибка: Счет не найден"
            
            if account.balance < amount:
                return f"Ошибка: Недостаточно средств. На счете: {account.balance}, требуется: {amount}"
            
            account.balance -= amount
            return f"Со счета снято {amount}. Новый баланс: {account.balance}"
        except BankError as b:
            return f"Ошибка при снятии средств: {b}"
    
    def transfer(self, from_account, to_account, amount):
        try:
            if amount <= 0:
                return "Ошибка: Сумма должна быть положительной"
            
            acc_from = self.accounts.get(from_account)
            acc_to = self.accounts.get(to_account)
            
            if not acc_from:
                return "Ошибка: Счет отправителя не найден"
            if not acc_to:
                return "Ошибка: Счет получателя не найден"
            if acc_from.balance < amount:
                return f"Ошибка: Недостаточно средств для перевода. На счете: {acc_from.balance}"
            if acc_from.currency != acc_to.currency:
                return "Ошибка: Перевод между разными валютами не поддерживается"
            
            acc_from.balance -= amount
            acc_to.balance += amount
            return f"Перевод {amount} {acc_from.currency} выполнен"
        except BankError as b:
            return f"Ошибка при переводе: {b}"
    
    def get_all_client_accounts(self, client_id):
        try:
            if client_id not in self.clients:
                return "Ошибка: Клиент не найден"
            
            return self.clients[client_id].accounts
        except BankError as b:
            return f"Ошибка при получении счетов: {b}"
    
    def generate_statement(self, client_id, filename=None):
        try:
            if client_id not in self.clients:
                return "Ошибка: Клиент не найден"
            
            client = self.clients[client_id]
            
            if not filename:
                filename = f"выписка_{client_id}.txt"
            
            #текстовый файл
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Банковская выписка\n")
                f.write("=" * 30 + "\n")
                f.write(f"Клиент: {client.name}\n")
                f.write(f"ID клиента: {client_id}\n")
                f.write("=" * 30 + "\n\n")
                
                total_balance = {}
                
                if not client.accounts:
                    f.write("У клиента нет открытых счетов\n")
                else:
                    f.write("Список счетов:\n")
                    f.write("-" * 30 + "\n")
                    
                    for currency, account in client.accounts.items():
                        f.write(f"Номер счета: {account.account_number}\n")
                        f.write(f"Валюта: {currency}\n")
                        f.write(f"Баланс: {account.balance:,.2f}\n")
                        f.write("-" * 30 + "\n")
                        
                        if currency in total_balance:
                            total_balance[currency] += account.balance
                        else:
                            total_balance[currency] = account.balance
                    
                    f.write("\nОбщий баланс:\n")
                    f.write("-" * 20 + "\n")
                    for currency, total in total_balance.items():
                        f.write(f"{currency}: {total:,.2f}\n")
            
            return f" Выписка сохранена в файл {filename}"
            
        except BankError as b:
            return f"Ошибка при создании выписки: {b}"

bank = Bank()
bank.create_client("001", "Иван Иванов")
bank.create_client("002", "Петр Петров")
bank.create_client("003", "Дмитрий Дмитриев")

def main():
    current_client = None
    
    while True:
        print("\n" + "-"*30)
        print("Банковская система")
        print("-"*30)
        
        if not current_client:
            print("1. Войти в систему")
            print("2. Выход")
        else:
            print(f"Добро пожаловать, {bank.clients[current_client].name}!")
            print("1. Открыть счет")
            print("2. Закрыть счет") 
            print("3. Пополнить счет")
            print("4. Снять деньги")
            print("5. Перевести деньги")
            print("6. Выписка по счетам")
            print("7. Мои счета")
            print("8. Выйти из системы")
        
        choice = input("Выберите действие: ").strip()
        
        if not current_client:
            if choice == "1":
                client_id = input("Введите ваш ID: ").strip()
                if client_id in bank.clients:
                    current_client = client_id
                    print("Успешный вход в систему!")
                else:
                    print("Клиент с таким ID не найден")
            elif choice == "2":
                print("До свидания!")
                break
            else:
                print("Неверный выбор")
        
        else:
            if choice == "1":
                currency = input("Введите валюту счета (RUB/USD/EUR): ").strip().upper()
                result = bank.open_account(current_client, currency)
                print(result)
            
            elif choice == "2":
                account_num = input("Введите номер счета: ").strip()
                result = bank.close_account(current_client, account_num)
                print(result)
            
            elif choice == "3":
                account_num = input("Введите номер счета: ").strip()
                try:
                    amount = float(input("Введите сумму: "))
                    result = bank.deposit(account_num, amount)
                    print(result)
                except ValueError:
                    print("Ошибка: Введите корректное число")
            
            elif choice == "4":
                account_num = input("Введите номер счета: ").strip()
                try:
                    amount = float(input("Введите сумму: "))
                    result = bank.withdraw(account_num, amount)
                    print(result)
                except ValueError:
                    print("Ошибка: Введите корректное число")
            
            elif choice == "5":
                from_acc = input("Введите номер счета отправителя: ").strip()
                to_acc = input("Введите номер счета получателя: ").strip()
                try:
                    amount = float(input("Введите сумму: "))
                    result = bank.transfer(from_acc, to_acc, amount)
                    print(result)
                except ValueError:
                    print("Ошибка: Введите корректное число")
            
            elif choice == "6":
                filename = input("Введите имя файла для выписки (или Enter для стандартного): ").strip()
                result = bank.generate_statement(current_client, filename)
                print(result)
                
                if not result.startswith("Ошибка:"):
                    try:
                        if not filename:
                            filename = f"выписка_{current_client}.txt"
                        print("\nСодержимое выписки:")
                        with open(filename, 'r', encoding='utf-8') as f:
                            print(f.read())
                    except BankError as b:
                        print(f"Не удалось прочитать файл: {b}")
            
            elif choice == "7":
                accounts = bank.get_client_accounts(current_client)
                if isinstance(accounts, str):  #если вернулась строка с ошибкой
                    print(accounts)
                else:
                    print("Ваши счета:")
                    for currency, account in accounts.items():
                        print(f"  {account.account_number}: {account.balance} {currency}")
            
            elif choice == "8":
                current_client = None
                print("Выход из системы выполнен")
            
            else:
                print("Неверный выбор")

if __name__ == "__main__":
    main()