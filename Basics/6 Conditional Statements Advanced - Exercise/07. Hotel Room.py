# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление
# цена за целият престой ? studio and apartment
month = input()  # May, June, July, August, September , October
nights = int(input())
studio_price = 0
apartment_price = 0
match month:
    case "May" | "October":
        if 7 < nights <= 14:
            studio_price = 50 * 0.95
        elif nights > 14:
            studio_price = 50 * 0.70
        else:
            studio_price = 50
        if nights > 14:
            apartment_price = 65 * 0.90
        else:
            apartment_price = 65
    case "June" | "September":
        if nights > 14:
            studio_price = 75.20 * 0.80
            apartment_price = 68.70 * 0.90
        else:
            studio_price = 75.20
            apartment_price = 68.70
    case "July" | "August":
        if nights > 14:
            studio_price = 76
            apartment_price = 77 * 0.90
        else:
            studio_price = 76
            apartment_price = 77
print(f"Apartment: {(nights * apartment_price):.2f} lv.")
print(f"Studio: {(nights * studio_price):.2f} lv.")
