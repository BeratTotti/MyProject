from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast(
    "Berat BETER",
    " Günaydın Herkese",
    duration= 20,
    icon_path = "icons8-chrome-94.png",
    threaded=True,
)
# şeklinde yapardık ve bu iconu kullanıcıdanda isteyebilirdik.