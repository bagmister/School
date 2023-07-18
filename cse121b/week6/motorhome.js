const currentDate = new Date()
var dd = String(currentDate.getDate()).padStart(2, '0');
var mm = String(currentDate.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = currentDate.getFullYear();
today = mm + '/' + dd + '/' + yyyy;
current_date = today

oil_changes_dictionary = {
    "most_recent_oil_change" : 0.00,
    "next_oil_change_millage" : 0.00,
    "replace_oil_by_if_milage_is_not_met_in_a_year": ""
}

previous_odometer_millage = 0.00
day_of_oil_change = "05/12/2023"
current_millage = 0

welcome_message = "Greetings! I am here to assist you with keeping track of your Motorhome maintanence."
window.alert(welcome_message)
function main(welcome_message){

    program_start(current_millage=current_millage, current_date=current_date)

}

function storeCurrentMillage(event){
    let current_millage = document.querySelector('#currentMillageMotorhome').value
    updateMessage = 'Updating current millage to: ' + current_millage
    window.alert(updateMessage);
    event.preventDefault()
    return current_millage
}

function calculate_next_year_to_change_oil_by(day_of_oil_change){
    if (day_of_oil_change == ""){
        day_of_oil_change = datetime.today()
    }
    oil_change_date_for_next_year = day_of_oil_change + dateutil.relativedelta(years=1)
    return oil_change_date_for_next_year
}

function get_next_oil_change_millage(last_oil_change, current_millage){
    if (last_oil_change == .0 || last_oil_change === ""){
        console.log("No recoreded last oil change date. Using current millage to base next oil change on.")
        next_oil_change = current_millage + 3000
    }
    else{
        console.log("Last recorded date for an oil change is: {last_oil_change}")
        next_oil_change = last_oil_change + 3000

    }  
    return next_oil_change
}

function update_oil_change(current_millage, current_date, day_of_oil_change){
    document.querySelector('#oilChangedoneToday').addEventListener("click",update_oil_change(current_millage, current_date, day_of_oil_change))
    if (day_of_oil_change == "" || 0.0){
        console.log("Oil change was not done today. let's update...")
        most_recent_oil_change = m_config.oil_changes_dictionary.get('most_recent_oil_change')
        next_oil_Change_millage = get_next_oil_change_millage(last_oil_change=most_recent_oil_change,  current_millage=current_millage)
        console.log("Updating milage to when next oil change needs to be done around.")
        m_config.oil_changes_dictionary.update({'next_oil_change_millage': next_oil_Change_millage})
        next_year_oil_cahnge_date = calculate_next_year_to_change_oil_by(day_of_oil_change)
        console.log("Updating date to replace oil by should millage not be reached.")
        m_config.oil_changes_dictionary.update({'replace_oil_by_if_milage_is_not_met_in_a_year': next_year_oil_cahnge_date})
    }
    else if (day_of_oil_change == current_date){
        console.log("Oil change was not done today. let's update...")
        m_config.oil_changes_dictionary.update({'most_recent_oil_change': float(current_millage)})
        console.log("Updating milage to when next oil change needs to be done around.")
        m_config.oil_changes_dictionary.update({'next_oil_change_millage': float(current_millage)})
        next_year_oil_cahnge_date = calculate_next_year_to_change_oil_by(day_of_oil_change)
        console.log("Updating date to replace oil by should millage not be reached.")
        m_config.oil_changes_dictionary.update({'replace_oil_by_if_milage_is_not_met_in_a_year': next_year_oil_cahnge_date})
    return

    }

}

function program_start(current_millage, current_date){
    program_entrance = input("What kind of maintannece would you like to find out next to do || update? Enter 'tires' for tire related. Enter chassis for the chassis and this includes drivetrain. Enter house for living area: ")
    if (program_entrance.lower() == "tires"){
        console.log("Entered: ${program_entrance}. Starting tires section... ")
        tires = tire_maintanenece(current_millage, current_date)
    }
    else if (program_entrance.lower() == "chassis"){
        console.log("Entered: {program_entrance}. Starting chassis section... ")
        chassis = chassis_maintanenece(current_millage, current_date)
    }
    else if (program_entrance.lower() == "house"){
        console.log("Entered: {program_entrance}. Starting house(living area box) section... ")
        chassis = house_maintanence(current_millage, current_date)

    }
    else{
        console.log("{program_entrance} is not a valid option. Would you like to enter maintanence?")
        continue_with_maintanence_entered = input("Enter 'y' for yes and 'n' for no: ")

    }
        return continue_with_maintanence_entered    

}

function updateCurrentOd(){
    console.log(currentMillage)
}

document.querySelector('#year').textContent = currentDate.getFullYear();