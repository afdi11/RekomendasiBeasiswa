def findDecision(obj): #obj[0]: NR1, obj[1]: NR2, obj[2]: NR3, obj[3]: NR4, obj[4]: NR5, obj[5]: NR6, obj[6]: NR7, obj[7]: IP, obj[8]: Penghasilan Orang Tua, obj[9]: Tanggungan Orang Tua, obj[10]: Tahun Masuk, obj[11]: Usia
   # {"feature": "Tahun Masuk", "instances": 236, "metric_value": 1.0, "depth": 1}
   if obj[10]>2015:
      # {"feature": "Tanggungan Orang Tua", "instances": 230, "metric_value": 0.9995, "depth": 2}
      if obj[9]<=7:
         # {"feature": "Penghasilan Orang Tua", "instances": 229, "metric_value": 0.9997, "depth": 3}
         if obj[8] == 'Golongan I':
            # {"feature": "Usia", "instances": 102, "metric_value": 0.9597, "depth": 4}
            if obj[11]>18:
               # {"feature": "NR4", "instances": 94, "metric_value": 0.979, "depth": 5}
               if obj[3] == '>2.8524752475247515':
                  # {"feature": "NR1", "instances": 81, "metric_value": 0.9946, "depth": 6}
                  if obj[0] == '>3.023100000000002':
                     # {"feature": "NR2", "instances": 75, "metric_value": 0.9896, "depth": 7}
                     if obj[1] == '>2.941818181818181':
                        # {"feature": "NR6", "instances": 74, "metric_value": 0.9868, "depth": 8}
                        if obj[5] == '>2.949595959595959':
                           # {"feature": "NR3", "instances": 73, "metric_value": 0.9836, "depth": 9}
                           if obj[2] == '>3.0298':
                              # {"feature": "NR5", "instances": 71, "metric_value": 0.9884, "depth": 10}
                              if obj[4] == '>2.8983333333333325':
                                 # {"feature": "NR7", "instances": 70, "metric_value": 0.9852, "depth": 11}
                                 if obj[6] == '>2.993299999999999':
                                    # {"feature": "IP", "instances": 69, "metric_value": 0.9877, "depth": 12}
                                    if obj[7] == '>3.152199999999997':
                                       return 'Iya'
                                    elif obj[7] == '<=3.152199999999997':
                                       return 'Iya'
                                    else:
                                       return 'Iya'
                                 elif obj[6] == '<=2.993299999999999':
                                    return 'Iya'
                                 else:
                                    return 'Iya'
                              elif obj[4] == '<=2.8983333333333325':
                                 return 'Tidak'
                              else:
                                 return 'Tidak'
                           elif obj[2] == '<=3.0298':
                              return 'Iya'
                           else:
                              return 'Iya'
                        elif obj[5] == '<=2.949595959595959':
                           return 'Tidak'
                        else:
                           return 'Tidak'
                     elif obj[1] == '<=2.941818181818181':
                        return 'Tidak'
                     else:
                        return 'Tidak'
                  elif obj[0] == '<=3.023100000000002':
                     # {"feature": "NR5", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[4] == '>2.8983333333333325':
                        # {"feature": "NR6", "instances": 5, "metric_value": 0.7219, "depth": 8}
                        if obj[5] == '>2.949595959595959':
                           return 'Tidak'
                        elif obj[5] == '<=2.949595959595959':
                           return 'Iya'
                        else:
                           return 'Iya'
                     elif obj[4] == '<=2.8983333333333325':
                        return 'Iya'
                     else:
                        return 'Iya'
                  else:
                     return 'Tidak'
               elif obj[3] == '<=2.8524752475247515':
                  # {"feature": "NR5", "instances": 13, "metric_value": 0.6194, "depth": 6}
                  if obj[4] == '>2.8983333333333325':
                     # {"feature": "NR3", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[2] == '>3.0298':
                        # {"feature": "NR2", "instances": 8, "metric_value": 0.5436, "depth": 8}
                        if obj[1] == '>2.941818181818181':
                           # {"feature": "NR1", "instances": 6, "metric_value": 0.65, "depth": 9}
                           if obj[0] == '>3.023100000000002':
                              # {"feature": "NR6", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[5] == '>2.949595959595959':
                                 # {"feature": "NR7", "instances": 6, "metric_value": 0.65, "depth": 11}
                                 if obj[6] == '>2.993299999999999':
                                    # {"feature": "IP", "instances": 6, "metric_value": 0.65, "depth": 12}
                                    if obj[7] == '>3.152199999999997':
                                       return 'Iya'
                                    else:
                                       return 'Iya'
                                 else:
                                    return 'Iya'
                              else:
                                 return 'Iya'
                           else:
                              return 'Iya'
                        elif obj[1] == '<=2.941818181818181':
                           return 'Iya'
                        else:
                           return 'Iya'
                     elif obj[2] == '<=3.0298':
                        return 'Tidak'
                     else:
                        return 'Tidak'
                  elif obj[4] == '<=2.8983333333333325':
                     return 'Iya'
                  else:
                     return 'Iya'
               else:
                  return 'Iya'
            elif obj[11]<=18:
               return 'Iya'
            else:
               return 'Iya'
         elif obj[8] == 'Golongan II':
            # {"feature": "Usia", "instances": 97, "metric_value": 0.9907, "depth": 4}
            if obj[11]>17:
               # {"feature": "NR1", "instances": 96, "metric_value": 0.9922, "depth": 5}
               if obj[0] == '>3.023100000000002':
                  # {"feature": "IP", "instances": 80, "metric_value": 0.971, "depth": 6}
                  if obj[7] == '>3.152199999999997':
                     # {"feature": "NR5", "instances": 79, "metric_value": 0.9663, "depth": 7}
                     if obj[4] == '>2.8983333333333325':
                        # {"feature": "NR3", "instances": 70, "metric_value": 0.9787, "depth": 8}
                        if obj[2] == '>3.0298':
                           # {"feature": "NR6", "instances": 69, "metric_value": 0.9742, "depth": 9}
                           if obj[5] == '>2.949595959595959':
                              # {"feature": "NR7", "instances": 63, "metric_value": 0.9587, "depth": 10}
                              if obj[6] == '>2.993299999999999':
                                 # {"feature": "NR2", "instances": 59, "metric_value": 0.9748, "depth": 11}
                                 if obj[1] == '>2.941818181818181':
                                    # {"feature": "NR4", "instances": 57, "metric_value": 0.973, "depth": 12}
                                    if obj[3] == '>2.8524752475247515':
                                       return 'Iya'
                                    elif obj[3] == '<=2.8524752475247515':
                                       return 'Tidak'
                                    else:
                                       return 'Tidak'
                                 elif obj[1] == '<=2.941818181818181':
                                    # {"feature": "NR4", "instances": 2, "metric_value": 1.0, "depth": 12}
                                    if obj[3] == '>2.8524752475247515':
                                       return 'Tidak'
                                    else:
                                       return 'Tidak'
                                 else:
                                    return 'Tidak'
                              elif obj[6] == '<=2.993299999999999':
                                 return 'Iya'
                              else:
                                 return 'Iya'
                           elif obj[5] == '<=2.949595959595959':
                              # {"feature": "NR4", "instances": 6, "metric_value": 0.9183, "depth": 10}
                              if obj[3] == '>2.8524752475247515':
                                 # {"feature": "NR7", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[6] == '>2.993299999999999':
                                    # {"feature": "NR2", "instances": 4, "metric_value": 1.0, "depth": 12}
                                    if obj[1] == '>2.941818181818181':
                                       return 'Tidak'
                                    else:
                                       return 'Tidak'
                                 elif obj[6] == '<=2.993299999999999':
                                    return 'Tidak'
                                 else:
                                    return 'Tidak'
                              elif obj[3] == '<=2.8524752475247515':
                                 return 'Tidak'
                              else:
                                 return 'Tidak'
                           else:
                              return 'Tidak'
                        elif obj[2] == '<=3.0298':
                           return 'Tidak'
                        else:
                           return 'Tidak'
                     elif obj[4] == '<=2.8983333333333325':
                        # {"feature": "NR3", "instances": 9, "metric_value": 0.7642, "depth": 8}
                        if obj[2] == '<=3.0298':
                           # {"feature": "NR4", "instances": 7, "metric_value": 0.5917, "depth": 9}
                           if obj[3] == '>2.8524752475247515':
                              return 'Iya'
                           elif obj[3] == '<=2.8524752475247515':
                              # {"feature": "NR7", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[6] == '>2.993299999999999':
                                 return 'Iya'
                              elif obj[6] == '<=2.993299999999999':
                                 return 'Tidak'
                              else:
                                 return 'Tidak'
                           else:
                              return 'Iya'
                        elif obj[2] == '>3.0298':
                           # {"feature": "NR7", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[6] == '>2.993299999999999':
                              return 'Tidak'
                           elif obj[6] == '<=2.993299999999999':
                              return 'Iya'
                           else:
                              return 'Iya'
                        else:
                           return 'Tidak'
                     else:
                        return 'Iya'
                  elif obj[7] == '<=3.152199999999997':
                     return 'Tidak'
                  else:
                     return 'Tidak'
               elif obj[0] == '<=3.023100000000002':
                  # {"feature": "NR7", "instances": 16, "metric_value": 0.896, "depth": 6}
                  if obj[6] == '>2.993299999999999':
                     # {"feature": "IP", "instances": 12, "metric_value": 0.65, "depth": 7}
                     if obj[7] == '<=3.152199999999997':
                        # {"feature": "NR2", "instances": 7, "metric_value": 0.8631, "depth": 8}
                        if obj[1] == '<=2.941818181818181':
                           # {"feature": "NR3", "instances": 5, "metric_value": 0.971, "depth": 9}
                           if obj[2] == '>3.0298':
                              # {"feature": "NR4", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[3] == '>2.8524752475247515':
                                 # {"feature": "NR5", "instances": 5, "metric_value": 0.971, "depth": 11}
                                 if obj[4] == '>2.8983333333333325':
                                    # {"feature": "NR6", "instances": 5, "metric_value": 0.971, "depth": 12}
                                    if obj[5] == '>2.949595959595959':
                                       return 'Tidak'
                                    else:
                                       return 'Tidak'
                                 else:
                                    return 'Tidak'
                              else:
                                 return 'Tidak'
                           else:
                              return 'Tidak'
                        elif obj[1] == '>2.941818181818181':
                           return 'Tidak'
                        else:
                           return 'Tidak'
                     elif obj[7] == '>3.152199999999997':
                        return 'Tidak'
                     else:
                        return 'Tidak'
                  elif obj[6] == '<=2.993299999999999':
                     # {"feature": "NR2", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1] == '>2.941818181818181':
                        return 'Iya'
                     elif obj[1] == '<=2.941818181818181':
                        # {"feature": "NR3", "instances": 2, "metric_value": 1.0, "depth": 8}
                        if obj[2] == '>3.0298':
                           # {"feature": "NR4", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[3] == '>2.8524752475247515':
                              # {"feature": "NR5", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[4] == '>2.8983333333333325':
                                 # {"feature": "NR6", "instances": 2, "metric_value": 1.0, "depth": 11}
                                 if obj[5] == '>2.949595959595959':
                                    # {"feature": "IP", "instances": 2, "metric_value": 1.0, "depth": 12}
                                    if obj[7] == '<=3.152199999999997':
                                       return 'Tidak'
                                    else:
                                       return 'Tidak'
                                 else:
                                    return 'Tidak'
                              else:
                                 return 'Tidak'
                           else:
                              return 'Tidak'
                        else:
                           return 'Tidak'
                     else:
                        return 'Tidak'
                  else:
                     return 'Iya'
               else:
                  return 'Tidak'
            elif obj[11]<=17:
               return 'Iya'
            else:
               return 'Iya'
         elif obj[8] == 'Golongan III':
            return 'Tidak'
         elif obj[8] == 'Golongan IV':
            return 'Tidak'
         elif obj[8] == 'Golongan V':
            return 'Tidak'
         elif obj[8] == 'Golongan VI':
            return 'Tidak'
         else:
            return 'Tidak'
      elif obj[9]>7:
         return 'Iya'
      else:
         return 'Iya'
   elif obj[10]<=2015:
      return 'Tidak'
   else:
      return 'Tidak'
