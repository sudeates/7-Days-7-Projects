import requests
import sys

def get_github_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n🚀 Kullanıcı: {data['name']}")
        print(f"📁 Kamu Repoları: {data['public_repos']}")
        print(f"👥 Takipçiler: {data['followers']}")
        print(f"📍 Konum: {data['location'] if data['location'] else 'Belirtilmemis'}")
        print(f"🔗 Link: {data['html_url']}\n")
    else:
        print("❌ Kullanıcı bulunamadı!")

if __name__ == "__main__":
    # Terminalden gelen argümanı kontrol et (mala anlatır gibi: sys.argv[1] yazılan isimdir)
    if len(sys.argv) > 1:
        user = sys.argv[1]
        get_github_info(user)
    else:
        print("⚠️ Kullanım: python analyzer.py <github_kullanici_adi>")