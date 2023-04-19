import requests
import cherrypy


class FhirEndpoint:
    PATIENT_ID_URL = 'https://hapi.fhir.org/baseR4/Patient?_id='

    @cherrypy.expose
    @cherrypy.tools.json_in()  # Позволяет автоматически распознавать JSON-данные в теле запроса
    def index(self):
        if cherrypy.request.method == "POST":
            bundle = cherrypy.request.json
            entries = bundle.get("entry", [])
            updated_entries = []
            for entry in entries:
                updated_entries.append(self.handle_entry(entry))
            bundle['entry'] = updated_entries
            return str(bundle)

    def handle_entry(self, entry):
        resource = entry.get("resource")
        if resource:
            if resource.get('resourceType') == 'Appointment':
                participants = resource.get("participant", [])
                for participant in participants:
                    actor = participant.get("actor")
                    reference = actor.get('reference')
                    if reference and reference.startswith('Patient/'):
                        actor_username = reference.replace('Patient/', '')
                        display_name = self.get_display_name(actor_username)
                        actor['display'] = display_name
                        participant['actor'] = actor

        return entry

    def get_display_name(self, username):
        url = self.PATIENT_ID_URL + username
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            entry = data.get("entry", [])
            recourse = entry[0]['resource']
            names = recourse.get('name')

            for name in names:
                if name.get('use') == 'official':
                    display_name = name.get('given')[0]

                    return display_name
        else:
            return None


if __name__ == "__main__":
    cherrypy.quickstart(FhirEndpoint(), '/')
