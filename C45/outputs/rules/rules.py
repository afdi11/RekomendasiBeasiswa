def findDecision(obj): #obj[0]: NR1, obj[1]: NR2, obj[2]: NR3, obj[3]: NR4, obj[4]: NR5, obj[5]: NR6, obj[6]: NR7, obj[7]: IP, obj[8]: Penghasilan Orang Tua, obj[9]: Tanggungan Orang Tua, obj[10]: Tahun Masuk, obj[11]: Usia
   # {"feature": "NR7", "instances": 296, "metric_value": 0.2231, "depth": 1}
   if obj[6] == '4':
      # {"feature": "NR1", "instances": 11, "metric_value": 0.1818, "depth": 2}
      if obj[0] == '3.61':
         # {"feature": "IP", "instances": 4, "metric_value": 0.3333, "depth": 3}
         if obj[7]>3.49:
            # {"feature": "NR2", "instances": 3, "metric_value": 0.3333, "depth": 4}
            if obj[1] == '3.61':
               # {"feature": "Usia", "instances": 2, "metric_value": 0.0, "depth": 5}
               if obj[11]<=20.0:
                  return 'Iya'
               elif obj[11]>20.0:
                  return 'Tidak'
               else:
                  return 'Tidak'
            elif obj[1] == '3.11':
               return 'Tidak'
            else:
               return 'Tidak'
         elif obj[7]<=3.49:
            return 'Iya'
         else:
            return 'Iya'
      elif obj[0] == '3.71':
         return 'Iya'
      elif obj[0] == '3.38':
         return 'Tidak'
      elif obj[0] == '3.34':
         return 'Tidak'
      elif obj[0] == '3.83':
         return 'Iya'
      elif obj[0] == '3.21':
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.89':
      # {"feature": "NR1", "instances": 10, "metric_value": 0.2, "depth": 2}
      if obj[0] == '3.41':
         # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 3}
         if obj[7]<=3.31:
            return 'Iya'
         elif obj[7]>3.31:
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[0] == '3.29':
         return 'Iya'
      elif obj[0] == '3.44':
         # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 3}
         if obj[7]>3.43:
            return 'Iya'
         elif obj[7]<=3.43:
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[0] == '3.42':
         return 'Tidak'
      elif obj[0] == '2.95':
         return 'Tidak'
      elif obj[0] == '2.39':
         return 'Tidak'
      elif obj[0] == '3.11':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.37':
      # {"feature": "NR1", "instances": 7, "metric_value": 0.1905, "depth": 2}
      if obj[0] == '3.88':
         # {"feature": "IP", "instances": 3, "metric_value": 0.3333, "depth": 3}
         if obj[7]>3.49:
            # {"feature": "Penghasilan Orang Tua", "instances": 2, "metric_value": 0.0, "depth": 4}
            if obj[8]>1500000.0:
               return 'Tidak'
            elif obj[8]<=1500000.0:
               return 'Iya'
            else:
               return 'Iya'
         elif obj[7]<=3.49:
            return 'Iya'
         else:
            return 'Iya'
      elif obj[0] == '3.19':
         return 'Iya'
      elif obj[0] == '2.71':
         return 'Tidak'
      elif obj[0] == '2.82':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.5':
      # {"feature": "NR1", "instances": 7, "metric_value": 0.1429, "depth": 2}
      if obj[0] == '3.41':
         # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 3}
         if obj[7]<=3.33:
            return 'Iya'
         elif obj[7]>3.33:
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[0] == '3.31':
         return 'Iya'
      elif obj[0] == '3.12':
         return 'Tidak'
      elif obj[0] == '3.38':
         return 'Tidak'
      elif obj[0] == '3.32':
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.88':
      # {"feature": "NR1", "instances": 6, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.94':
         return 'Iya'
      elif obj[0] == '3.56':
         return 'Tidak'
      elif obj[0] == '2.79':
         return 'Tidak'
      elif obj[0] == '3.06':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.61':
      # {"feature": "NR1", "instances": 6, "metric_value": 0.1667, "depth": 2}
      if obj[0] == '3.65':
         # {"feature": "Penghasilan Orang Tua", "instances": 2, "metric_value": 0.0, "depth": 3}
         if obj[8]>2000000.0:
            return 'Iya'
         elif obj[8]<=2000000.0:
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[0] == '3.71':
         return 'Tidak'
      elif obj[0] == '3.63':
         return 'Tidak'
      elif obj[0] == '3.09':
         return 'Tidak'
      elif obj[0] == '3.88':
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.64':
      return 'Tidak'
   elif obj[6] == '3.74':
      return 'Iya'
   elif obj[6] == '3':
      # {"feature": "IP", "instances": 5, "metric_value": 0.0, "depth": 2}
      if obj[7]<=3.55:
         return 'Tidak'
      elif obj[7]>3.55:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.71':
      # {"feature": "IP", "instances": 5, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.52:
         return 'Iya'
      elif obj[7]<=3.52:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.25':
      # {"feature": "IP", "instances": 5, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.12:
         return 'Iya'
      elif obj[7]<=3.12:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.4':
      # {"feature": "NR1", "instances": 5, "metric_value": 0.2, "depth": 2}
      if obj[0] == '3.47':
         # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 3}
         if obj[7]>3.23:
            return 'Tidak'
         elif obj[7]<=3.23:
            return 'Iya'
         else:
            return 'Iya'
      elif obj[0] == '3.76':
         return 'Iya'
      elif obj[0] == '3.12':
         return 'Tidak'
      elif obj[0] == '3.56':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.65':
      # {"feature": "Penghasilan Orang Tua", "instances": 4, "metric_value": 0.0, "depth": 2}
      if obj[8]<=2504522.0:
         return 'Iya'
      elif obj[8]>2504522.0:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.53':
      # {"feature": "NR1", "instances": 4, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.65':
         return 'Iya'
      elif obj[0] == '3.76':
         return 'Tidak'
      elif obj[0] == '3':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.14':
      # {"feature": "Penghasilan Orang Tua", "instances": 4, "metric_value": 0.0, "depth": 2}
      if obj[8]<=1500000.0:
         return 'Iya'
      elif obj[8]>1500000.0:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.79':
      # {"feature": "IP", "instances": 4, "metric_value": 0.3333, "depth": 2}
      if obj[7]>3.07:
         # {"feature": "NR1", "instances": 3, "metric_value": 0.3333, "depth": 3}
         if obj[0] == '3.76':
            # {"feature": "Usia", "instances": 2, "metric_value": 0.0, "depth": 4}
            if obj[11]>19.0:
               return 'Tidak'
            elif obj[11]<=19.0:
               return 'Iya'
            else:
               return 'Iya'
         elif obj[0] == '2.58':
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[7]<=3.07:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.56':
      # {"feature": "IP", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.62:
         return 'Iya'
      elif obj[7]<=3.62:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.67':
      return 'Iya'
   elif obj[6] == '3.75':
      # {"feature": "Penghasilan Orang Tua", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[8]<=2221200.0:
         return 'Tidak'
      elif obj[8]>2221200.0:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '2.8':
      # {"feature": "IP", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.58:
         return 'Iya'
      elif obj[7]<=3.58:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.83':
      # {"feature": "IP", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[7]<=3.78:
         return 'Iya'
      elif obj[7]>3.78:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.48':
      # {"feature": "Tanggungan Orang Tua", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[9]<=3.0:
         return 'Tidak'
      elif obj[9]>3.0:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.21':
      # {"feature": "Usia", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[11]>18.0:
         return 'Tidak'
      elif obj[11]<=18.0:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.6':
      # {"feature": "NR1", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.42':
         return 'Tidak'
      elif obj[0] == '3.37':
         return 'Iya'
      elif obj[0] == '3.12':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.57':
      return 'Iya'
   elif obj[6] == '3.58':
      # {"feature": "NR1", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.71':
         return 'Iya'
      elif obj[0] == '2.61':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.76':
      # {"feature": "IP", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.51:
         return 'Tidak'
      elif obj[7]<=3.51:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.72':
      return 'Tidak'
   elif obj[6] == '3.42':
      # {"feature": "NR1", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.71':
         return 'Tidak'
      elif obj[0] == '3.12':
         return 'Iya'
      elif obj[0] == '3.39':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '2.67':
      # {"feature": "NR1", "instances": 3, "metric_value": 0.0, "depth": 2}
      if obj[0] == '2.97':
         return 'Iya'
      elif obj[0] == '3.12':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.46':
      return 'Iya'
   elif obj[6] == '3.08':
      return 'Iya'
   elif obj[6] == '3.26':
      return 'Tidak'
   elif obj[6] == '3.52':
      # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[7]<=3.44:
         return 'Iya'
      elif obj[7]>3.44:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.19':
      # {"feature": "Penghasilan Orang Tua", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[8]>1500000.0:
         return 'Tidak'
      elif obj[8]<=1500000.0:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.94':
      return 'Iya'
   elif obj[6] == '3.29':
      return 'Tidak'
   elif obj[6] == '0':
      # {"feature": "NR1", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.82':
         return 'Tidak'
      elif obj[0] == '3.06':
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '1.76':
      return 'Iya'
   elif obj[6] == '3.9':
      return 'Iya'
   elif obj[6] == '3.1':
      # {"feature": "NR1", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.59':
         return 'Iya'
      elif obj[0] == '2.74':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.11':
      return 'Iya'
   elif obj[6] == '3.78':
      return 'Iya'
   elif obj[6] == '3.59':
      # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.52:
         return 'Tidak'
      elif obj[7]<=3.52:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '3.22':
      # {"feature": "NR1", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.29':
         return 'Tidak'
      elif obj[0] == '3.69':
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '2.5':
      return 'Iya'
   elif obj[6] == '3.73':
      return 'Iya'
   elif obj[6] == '3.16':
      # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[7]<=3.45:
         return 'Tidak'
      elif obj[7]>3.45:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '2.89':
      # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[7]<=3.02:
         return 'Iya'
      elif obj[7]>3.02:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.63':
      return 'Tidak'
   elif obj[6] == '3.84':
      # {"feature": "NR1", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3':
         return 'Tidak'
      elif obj[0] == '3.06':
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '2.58':
      # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.7:
         return 'Tidak'
      elif obj[7]<=3.7:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[6] == '2.26':
      # {"feature": "IP", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[7]>3.07:
         return 'Iya'
      elif obj[7]<=3.07:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.45':
      return 'Iya'
   elif obj[6] == '3.39':
      return 'Tidak'
   elif obj[6] == '2.61':
      return 'Tidak'
   elif obj[6] == '3.31':
      return 'Tidak'
   elif obj[6] == '3.68':
      return 'Iya'
   elif obj[6] == '3.17':
      # {"feature": "NR1", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.39':
         return 'Iya'
      elif obj[0] == '2.79':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '3.85':
      # {"feature": "NR1", "instances": 2, "metric_value": 0.0, "depth": 2}
      if obj[0] == '3.19':
         return 'Iya'
      elif obj[0] == '2.42':
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6] == '2.75':
      return 'Tidak'
   elif obj[6] == '1.92':
      return 'Tidak'
   elif obj[6] == '2.87':
      return 'Tidak'
   elif obj[6] == '3.62':
      return 'Tidak'
   elif obj[6] == '3.69':
      return 'Tidak'
   elif obj[6] == '3.3':
      return 'Tidak'
   elif obj[6] == '3.04':
      return 'Tidak'
   elif obj[6] == '2.82':
      return 'Tidak'
   elif obj[6] == '3.8':
      return 'Iya'
   elif obj[6] == '2.4':
      return 'Tidak'
   elif obj[6] == '3.2':
      return 'Tidak'
   elif obj[6] == '3.86':
      return 'Tidak'
   elif obj[6] == '3.33':
      return 'Tidak'
   elif obj[6] == '3.41':
      return 'Tidak'
   elif obj[6] == '3.43':
      return 'Tidak'
   elif obj[6] == '2.92':
      return 'Iya'
   elif obj[6] == '2.95':
      return 'Tidak'
   elif obj[6] == '2.88':
      return 'Iya'
   elif obj[6] == '2.85':
      return 'Iya'
   elif obj[6] == '3.95':
      return 'Iya'
   elif obj[6] == '3.06':
      return 'Tidak'
   elif obj[6] == '2.44':
      return 'Iya'
   elif obj[6] == '3.82':
      return 'Tidak'
   elif obj[6] == '3.03':
      return 'Tidak'
   elif obj[6] == '3.36':
      return 'Tidak'
   elif obj[6] == '3.81':
      return 'Tidak'
   elif obj[6] == '3.27':
      return 'Iya'
   elif obj[6] == '3.07':
      return 'Tidak'
   else:
      return 'Tidak'
