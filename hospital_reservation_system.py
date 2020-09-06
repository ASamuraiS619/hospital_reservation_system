class Clinic():
    def __init__(self, patient_list=[]):
        self.patient_list = patient_list

    def show_waiting_count(self):
        print("現在の待ち人数 {}人".format(len(self.patient_list)))

    def reserve(self, patient):
        if self._check_reserved(patient):
            print("予約済みです")
        else:
            self.patient_list.append(patient)
            print('予約しました。')
            self.show_waiting_count()

    def diagnosis(self, patient=None):
        if patient is not None:
            print("{}さん　診察".format(patient.name))
            self.patient_list.remove(patient)
        else:
            print("{}さん　診察".format(self.patient_list[0].name))
            del self.patient_list[0]

    def _check_reserved(self, patient):
        return patient in self.patient_list

class Human():
    def __init__(self, name):
        self.name = name


class Patient(Human):
    def __init__(self, name, symptom, patient_id):
        super().__init__(name)

        self.symptom = symptom
        self.patient_id = patient_id

myclinic = Clinic()

sato = Patient('佐藤', 111, '咳')
tanaka = Patient('田中', 222, '腹痛')
suzuki = Patient('鈴木', 333, '鼻水')
yamada = Patient('山田', 444, '倦怠感')
taguchi = Patient('田口', 555, '頭痛')

for patient in [sato, tanaka, suzuki, yamada, taguchi]:
    myclinic.reserve(patient)

myclinic.show_waiting_count()

myclinic.reserve(sato)

myclinic.diagnosis()
myclinic.show_waiting_count()

myclinic.diagnosis(taguchi)
myclinic.show_waiting_count()

myclinic.patient_list
