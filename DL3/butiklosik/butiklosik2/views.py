from django.shortcuts import render

# Create your views here.
def pelanggan(request) :
    allpelangganobj = models.pelanggan.objects.all()
    getpelangganobj = models.pelanggan.objects.get(idpelanggan=1)
    filterpelangganobj = models.pelanggan.objects.filter(jeniskelamin = 'Perempuan')


    return render(request, 'pelanggan.html' , {
        "allpelangganobj" : allpelangganobj,
        "getpelangganobj" : getpelangganobj,
        "filterpelangganobj" : filterpelangganobj
    })

def createdatapelanggan(request) :
    if request.method == 'GET' :
        return render(request, 'createdata.html')
    else :
        idpelanggan = request.POST['idpelanggan']
        nama = request.POST['nama']
        jeniskelamin = request.POST['jeniskelamin']
        nohandphone = request.POST['nohandphone']
        alamat = request.POST['alamat']

        newpelanggan = models.pelanggan(
            idpelanggan = idpelanggan,
            nama = nama,
            jeniskelamin = jeniskelamin,
            nohandphone = nohandphone,
            alamat = alamat
        ).save()
        return redirect('pelanggan')

        