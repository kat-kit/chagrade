var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var CHAGRADE = {
    URLS: []  // Set in base.html
}

CHAGRADE.api = {
    request: function (method, url, data) {
        return $.ajax({
            type: method,
            url: url,
            data: JSON.stringify(data),
            //headers:{"X-CSRFToken": csrf_token},
            contentType: "application/json",
            dataType: 'json'
        })
    },
    // search: function (filters) {
    //     // get existing params and update them with the filters
    //     var params = route.query()
    //     Object.assign(params, filters)
    //     // Remove any unused params so our URL stays pretty
    //     dict_remove_empty_values(params)
    //     // Add query params to URL
    //     // This causes bugs with repeating the query params over and over, so we just replaceState now
    //     //route('?' + $.param(params))
    //     window.history.replaceState("", "", `?${$.param(params)}`);
    //
    //     return CHAGRADE.api.request('GET', URLS.API + "query/?" + $.param(params))
    // },
    // ------------------------------------------------------------------------
    // // Producers
    // get_producers: function() {
    //     return CHAGRADE.api.request('GET', URLS.API + "producers/")
    // },
    // create_producer: function(data) {
    //     return CHAGRADE.api.request('POST', URLS.API + "producers/", data)
    // },
    // update_producer: function(pk, data) {
    //     return CHAGRADE.api.request('PUT', URLS.API + "producers/" + pk + "/", data)
    // },
    // delete_producer: function(pk) {
    //     return CHAGRADE.api.request('DELETE', URLS.API + "producers/" + pk + "/")
    // }
    get_klass: function(pk) {
        return CHAGRADE.api.request('GET', URLS.API + 'klasses/' + pk)
    },
    get_klasses: function() {
        return CHAGRADE.api.request('GET', URLS.API + 'klasses/')
    },
    activate_klass: function(pk) {
        return CHAGRADE.api.request('POST', '/klasses/wizard/' + pk + '/activate')
    },
    message_klass_students: function(pk, data) {
        return CHAGRADE.api.request('POST', '/klasses/email_students/' + pk + '/', data)
    },
    //Students
    create_student: function(data) {
        return CHAGRADE.api.request('POST', URLS.API + "students/", data)
    },
    create_single_student: function(data) {
        return CHAGRADE.api.request('POST', URLS.API + "create_student/", data)
    },
    get_student: function(pk) {
        return CHAGRADE.api.request('GET', URLS.API + "students/" + pk)
    },
    update_student: function(pk, data) {
        return CHAGRADE.api.request('PUT', URLS.API + 'students/' + pk + "/", data)
    },
    // Definitions
    get_definition: function(pk) {
        return CHAGRADE.api.request('GET', URLS.API + "definitions/" + pk)
    },
    create_definition: function(data) {
        return CHAGRADE.api.request('POST', URLS.API + 'definitions/', data)
    },
    update_definition: function(pk, data) {
        return CHAGRADE.api.request('PUT', URLS.API + 'definitions/' + pk + "/", data)
    },
    // Questions
    delete_question: function(pk) {
        return CHAGRADE.api.request('DELETE', URLS.API + "questions/" + pk + "/")
    },
    // Criteria
    delete_criteria: function(pk) {
        return CHAGRADE.api.request('DELETE', URLS.API + "criterias/" + pk + "/")
    },
    // Submissions
    create_submission: function(data) {
        return CHAGRADE.api.request('POST', URLS.API + "submissions/", data)
    },
    get_submission: function(pk) {
        return CHAGRADE.api.request('GET', URLS.API + "submissions/" + pk)
    },
    // Grades
    create_grade: function(data) {
        return CHAGRADE.api.request('POST', URLS.API + "grades/", data)
    },
    get_grade: function(pk) {
        return CHAGRADE.api.request('GET', URLS.API + "grades/" + pk)
    },
    update_grade: function(pk, data) {
        return CHAGRADE.api.request('PUT', URLS.API + 'grades/' + pk + "/", data)
    },
    // Teams
    get_teams: function() {
        return CHAGRADE.api.request('GET', URLS.API + 'teams/')
    },
    get_team: function(pk) {
        return CHAGRADE.api.request('GET', URLS.API + 'teams/' + pk)
    },
    create_team: function(data) {
        return CHAGRADE.api.request('POST', URLS.API + 'teams/', data)
    },
    update_team: function(pk, data) {
        return CHAGRADE.api.request('PUT', URLS.API + 'teams/' + pk + "/", data)
    },
    delete_team: function(pk) {
        return CHAGRADE.api.request('DELETE', URLS.API + "teams/" + pk + "/")
    },
}
