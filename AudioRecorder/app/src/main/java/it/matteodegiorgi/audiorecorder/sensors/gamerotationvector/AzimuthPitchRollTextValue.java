package it.matteodegiorgi.audiorecorder.sensors.gamerotationvector;

/*enum used for the different text values that azimuth pitch and roll can have*/
public enum AzimuthPitchRollTextValue {
    NORTH {
        @Override
        public String toString ( ) {
            return "NORTH";
        }
    }, EAST {
        @Override
        public String toString ( ) {
            return "EAST";
        }
    }, SOUTH {
        @Override
        public String toString ( ) {
            return "SOUTH";
        }
    }, WEST {
        @Override
        public String toString ( ) {
            return "WEST";
        }
    }, NORTHEAST {
        @Override
        public String toString ( ) {
            return "NORTHEAST";
        }
    }, SOUTHEAST {
        @Override
        public String toString ( ) {
            return "SOUTHEAST";
        }
    }, SOUTHWEST {
        @Override
        public String toString ( ) {
            return "SOUTHWEST";
        }
    }, NORTHWEST {
        @Override
        public String toString ( ) {
            return "NORTHWEST";
        }
    }
}
