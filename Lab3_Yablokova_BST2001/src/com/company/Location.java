package com.company;

public class Location {
    /** Координата X. **/
    public int xCoord;

    /** Координата Y. **/
    public int yCoord;


    /** Конструктор, который дает объекту координаты. **/
    public Location(int x, int y)
    {
        xCoord = x;
        yCoord = y;
    }

    /** Создает новую локацию с координатами (0, 0). **/
    public Location()
    {
        this(0, 0);
    }
    /** Сравнивает определенную локацию с текущей. **/
    public boolean equals(Object obj) {

        // Проверка приналежности объекта obj к классу Location
        if (obj instanceof Location) {

            // Каст другого объекта к классу Location,
            // потом сравнение.  Возвращает true если равны.
            Location other = (Location) obj;
            if (xCoord == other.xCoord && yCoord == other.yCoord) {
                return true;
            }
        }
        // Если мы попали сюда - координаты не равны.  Возвращает false.
        return false;
    }

    /** Обеспечивает hashCode для каждой локации. **/
    public int hashCode() {
        int result = 20; // Какое-то число
        // Используем другое число для умножения
        result = 30 * result + xCoord;
        result = 30 * result + yCoord;
        return result;
    }
}
