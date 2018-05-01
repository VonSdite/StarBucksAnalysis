from calcDistance import calcDistance

def FindRange(csv_file, longitude, latitude, range):
    csv_file['Distance'] = csv_file.apply(
        lambda x:calcDistance(longitude, latitude, x.Longitude, x.Latitude),
                              axis=1)

    return csv_file[csv_file['Distance'] <= range]