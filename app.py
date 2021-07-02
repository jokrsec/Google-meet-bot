from pages import GoogleLoginPage, JoinMeet



g_page = GoogleLoginPage()

g_page.login()


meeting_link = "https://meet.google.com/ren-dpaw-sma"

m_page = JoinMeet()
m_page.join(meeting_link)






