//
//  Basurero.swift
//  User-Location
//
//  Created by Pabelco Zambrano Vélez on 1/24/20.
//  Copyright © 2020 Sean Allen. All rights reserved.
//

import Foundation
enum TrashError:Error{
    case noDataAvailable
    case canNotProcessData
}
struct Trash: Decodable {
    let trashes:[Model]
}
struct Model :Decodable{
    let model:String
    let pk:Int
    let fields:Trashes
}
struct Trashes:Decodable {
    let name:String
    let latitud:String
    let longitud:String
    let horaInicio:String
    let horaFin:String
    let calificacion:Double
    
    
    static let basePath = "http://127.0.0.1:8000/LocateTrash/trashes"
    
    static func getTrashCans ( completion: @escaping (Result<[Trashes],TrashError>) -> Void) {
        
        let url = basePath
        let request = URLRequest(url: URL(string: url)!)
        
        let task = URLSession.shared.dataTask(with: request) {data,
            _, _  in
            guard let json = data else {
                completion(.failure(.noDataAvailable))
                return
            }
            do{
                let decoder = JSONDecoder()
                print("F")
                let trashesResponse = try decoder.decode([Trash].self, from: json)
                print("a")
                var bigtrash :[Trashes] = []
                for tR in trashesResponse{
                let trashcCans = tR.trashes
                    for t in trashcCans{
                        let trash = t.fields
//                        for tc in trash{
                            bigtrash.append(trash)
//                        }
                    }
                }
                completion(.success(bigtrash))
            }catch{
                completion(.failure(.canNotProcessData))
            }
            
            
//            var trashesArray:[Trashes] = []
//
//            if let data = data {
//                do {
//                    if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String:Any] {
//                        print(json)
//
//                        }
//
//                }catch {
//                    print(error.localizedDescription)
//                    print("F")
//                }
////              completion(trashesArray)
//            }
        }
        task.resume()
    }
}
