//
//  MapScreen.swift
//  User-Location
//
//  Created by Sean Allen on 8/24/18.
//  Copyright © 2018 Sean Allen. All rights reserved.
//

import UIKit
import MapKit
import CoreLocation


class customPin: NSObject, MKAnnotation {
    var coordinate: CLLocationCoordinate2D
    var title: String?
    var subtitle: String?
    
    init(pinTitle:String, pinSubTitle:String, location:CLLocationCoordinate2D) {
        self.title = pinTitle
        self.subtitle = pinSubTitle
        self.coordinate = location
    }
}

class MapScreen: UIViewController {
    
    
    @IBOutlet weak var mapView: MKMapView!

    @IBOutlet var trailingMV: NSLayoutConstraint!
    
    @IBOutlet var leadingMV: NSLayoutConstraint!
    
    var menuOut = false
    
    var listOfTrashCans = [Trashes]()
    
    
    @IBAction func menuTapped(_ sender: UIButton) {
        if !menuOut {
            leadingMV.constant = 150
            trailingMV.constant = -150
            menuOut = true
        } else {
            leadingMV.constant = 0
            trailingMV.constant = 0
            menuOut = false
        }
        
        UIView.animate(withDuration: 0.2, delay: 0.0, options: .curveEaseIn, animations: {
            self.view.layoutIfNeeded()
        }) { (animationComplete) in
            print("The animation is complete!")
        }
    }
    
    let locationManager = CLLocationManager()
    let regionInMeters: Double = 1000
    
    override func viewDidLoad() {
        super.viewDidLoad()
        checkLocationServices()
    }
    
    
    func setupLocationManager() {
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
    }
    
    
    func centerViewOnUserLocation() {
        if let location = locationManager.location?.coordinate {
            let region = MKCoordinateRegion.init(center: location, latitudinalMeters: regionInMeters, longitudinalMeters: regionInMeters)
            mapView.setRegion(region, animated: true)
        }
    }
    
    
    func checkLocationServices() {
        
        Trashes.getTrashCans{
            [weak self] result in
            switch result {
            case .failure(let error):
                print(error)
            case .success(let trashes):
                self?.listOfTrashCans = trashes
            }
        }
        print(listOfTrashCans.count)
        for t in listOfTrashCans{
            makePinTrash(name: t.name, latitud: t.latitud, longitud: t.longitud, calificacion: t.calificacion)
        }
        if CLLocationManager.locationServicesEnabled() {
            setupLocationManager()
            checkLocationAuthorization()
//            putTrahsCans()

//            makePinTrash(name: "F", latitud: "-2.1386603", longitud:"-79.906885", calificacion: "0.0")
        } else {
            // Show alert letting the user know they have to turn this on.
        }
    }
    
    
    func checkLocationAuthorization() {
        switch CLLocationManager.authorizationStatus() {
        case .authorizedWhenInUse:
            mapView.showsUserLocation = true
            centerViewOnUserLocation()
            locationManager.startUpdatingLocation()
            break
        case .denied:
            // Show alert instructing them how to turn on permissions
            break
        case .notDetermined:
            locationManager.requestWhenInUseAuthorization()
        case .restricted:
            // Show an alert letting them know what's up
            break
        case .authorizedAlways:
            break
        @unknown default:
            print("F")
        }
    }
    
    func putTrahsCans(){
        Trashes.getTrashCans{
            [weak self] result in
            switch result {
            case .failure(let error):
                print(error)
            case .success(let trashes):
                self?.listOfTrashCans = trashes
            }
        }
    }
    
    func makePinTrash(name: String, latitud:String, longitud:String, calificacion:Double){
        print(latitud,longitud)
        let lat = Double(latitud)
        let long = Double(longitud)
        let location = CLLocationCoordinate2D(latitude: lat!, longitude:long!)
        let pin = customPin(pinTitle: name, pinSubTitle: String(calificacion), location: location)
        mapView.addAnnotation(pin)
    }
}


extension MapScreen: CLLocationManagerDelegate {
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let location = locations.last else { return }
        let region = MKCoordinateRegion.init(center: location.coordinate, latitudinalMeters: regionInMeters, longitudinalMeters: regionInMeters)
        mapView.setRegion(region, animated: true)
    }
    
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        checkLocationAuthorization()
    }
}


