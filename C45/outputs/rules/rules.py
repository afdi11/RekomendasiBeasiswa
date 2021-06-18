def findDecision(obj): #obj[0]: NR1, obj[1]: NR2, obj[2]: NR3, obj[3]: NR4, obj[4]: NR5, obj[5]: IP, obj[6]: Penghasilan Orang Tua, obj[7]: Tanggungan Orang Tua, obj[8]: Tahun Masuk, obj[9]: Usia
   # {"feature": "Penghasilan Orang Tua", "instances": 236, "metric_value": 1.0, "depth": 1}
   if obj[6]<=3830075.4017789913:
      # {"feature": "NR2", "instances": 211, "metric_value": 0.9898, "depth": 2}
      if obj[1]>2.2882933425304444:
         # {"feature": "NR5", "instances": 208, "metric_value": 0.9869, "depth": 3}
         if obj[4]>1.68:
            # {"feature": "NR4", "instances": 207, "metric_value": 0.9858, "depth": 4}
            if obj[3]>2.159527649612246:
               # {"feature": "IP", "instances": 204, "metric_value": 0.9883, "depth": 5}
               if obj[5]<=3.8923561573092824:
                  # {"feature": "Usia", "instances": 202, "metric_value": 0.9898, "depth": 6}
                  if obj[9]>17.0:
                     # {"feature": "NR1", "instances": 200, "metric_value": 0.9913, "depth": 7}
                     if obj[0]>2.58:
                        # {"feature": "NR3", "instances": 199, "metric_value": 0.992, "depth": 8}
                        if obj[2]>2.61:
                           # {"feature": "Tanggungan Orang Tua", "instances": 198, "metric_value": 0.9926, "depth": 9}
                           if obj[7]<=7.0:
                              # {"feature": "Tahun Masuk", "instances": 197, "metric_value": 0.9933, "depth": 10}
                              if obj[8]>2016.0:
                                 return 'Iya'
                              elif obj[8]<=2016.0:
                                 return 'Tidak'
                              else:
                                 return 'Tidak'
                           elif obj[7]>7.0:
                              return 'Iya'
                           else:
                              return 'Iya'
                        elif obj[2]<=2.61:
                           return 'Iya'
                        else:
                           return 'Iya'
                     elif obj[0]<=2.58:
                        return 'Iya'
                     else:
                        return 'Iya'
                  elif obj[9]<=17.0:
                     return 'Iya'
                  else:
                     return 'Iya'
               elif obj[5]>3.8923561573092824:
                  return 'Iya'
               else:
                  return 'Iya'
            elif obj[3]<=2.159527649612246:
               return 'Iya'
            else:
               return 'Iya'
         elif obj[4]<=1.68:
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[1]<=2.2882933425304444:
         return 'Tidak'
      else:
         return 'Tidak'
   elif obj[6]>3830075.4017789913:
      return 'Tidak'
   else:
      return 'Tidak'
